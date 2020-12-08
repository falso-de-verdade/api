'''
Handles user creation.
'''

from . import utils
from ..crypto import hasher
from eve.utils import config
from eve.methods.common import (
    marshal_write_response,
    build_response_document,
)
from flask import Blueprint, current_app as app

# main blueprint app
blueprint = Blueprint('user_creation', __name__, url_prefix='/signup')

# domain resource
resource = 'user'


@blueprint.route('/resident', methods=['POST'])
def resident_signup():
    '''
    Sign up residents into application.
    '''

    resident_role = {
        'role': ['resident']
    }

    return common_user_creation(resident_role)


@blueprint.route('/manager', methods=['POST'])
def manager_signup():
    '''
    Sign up managers into application.
    '''

    manager_role = {
        'role': ['manager']
    }

    return common_user_creation(manager_role)


def common_user_creation(additional_data):
    '''
    Common user creation process.
    '''

    schema = {
        'type': 'object',
        'properties': {
            'email': {
                'type': 'string',
                'format': 'email',
            },
            'name': {
                'type': 'string',
            },
            'password': {
                'type': 'string',
                'minLength': 8,
            },
        },
        'required': [
            'email',
            'name',
            'password',
        ]
    }

    # parse payload data
    data = utils.validate_json_request(schema)

    # hash user password
    data['passwdHash'] = hasher.hash(data['password'])

    # discard cleartext password
    del data['password']

    # add static data
    data.update(additional_data)

    # create user and get first object id returned
    _id = app.data.insert(resource, data)[0]

    # grab resource id field
    id_field = config.DOMAIN[resource]['id_field']

    # get user by _id
    document = app.data.find_one_raw(resource, **{ id_field: _id })

    # serialize ObjectId
    document[id_field] = str(document[id_field])

    # build the full response document
    result = document
    build_response_document(result, resource, [], document)

    # add extra write meta data
    result[config.STATUS] = config.STATUS_OK

    # limit what actually gets sent to minimize bandwidth usage
    response = marshal_write_response(result, resource)

    return response, 201
