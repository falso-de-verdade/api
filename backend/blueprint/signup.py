'''
Handles user creation.
'''

from . import utils
from ..crypto import hasher
from eve.methods.post import post_internal
from eve.utils import config
from flask import (
    abort,
    Blueprint, 
    current_app as app
)

from datetime import timedelta, datetime, timezone

# main blueprint app
blueprint = Blueprint('user_creation', __name__, url_prefix='/signup')

# domain resource
resource = 'user'


@blueprint.route('/resident', methods=['POST'])
def resident_signup():
    '''
    Sign up residents into application.
    '''

    def add_resident(data):
        data['role'] = ['resident']

    def add_condominium(data):
        condominium = find_condominium_or_fail(data['token'])
        data['condominium'] = condominium

    def add_requirements(data):
        add_resident(data)
        add_condominium(data)

    custom_schema = validation_schema()

    # insert token field
    custom_schema['properties']['token'] = {
        'type': 'string',
    }

    custom_schema['required'].append('token')

    return common_user_creation(add_requirements, 
                                schema=custom_schema)


@blueprint.route('/manager', methods=['POST'])
def manager_signup():
    '''
    Sign up managers into application.
    '''

    def add_manager(data):
        data['role'] = ['manager']

    return common_user_creation(add_manager)


def common_user_creation(with_data, schema=None):
    '''
    Common user creation process.
    '''

    schema = schema or validation_schema()

    # parse payload data
    data = utils.validate_json_request(schema)

    # hash user password
    data['passwdHash'] = hasher.hash(data['password'])

    # discard cleartext password
    del data['password']

    # transform current data
    with_data(data)

    # create user and get first object id returned
    response, _, _, status, _ = post_internal(resource, payl=data)
    return response, status


def find_condominium_or_fail(token):
    '''
    Try to find a condominium from invite token.
    '''

    invite = app.data.find_one_raw('invite', **{ 'token': token })

    # ensure token exists
    if invite is None:
        abort(422, 'Unknow token')

    # calculate how many time has gone
    elapsed = datetime.now(timezone.utc) - invite['_created']

    if elapsed > timedelta(minutes=config.INVITE_LIFETIME):
        abort(422, 'Unknow token')

    # remove token
    id_field = config.DOMAIN['invite']['id_field']
    app.data.remove('invite', { id_field: invite['_id'] })

    return invite['condominium']

    
def validation_schema():
    '''
    Default validation schema.
    '''

    return {
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