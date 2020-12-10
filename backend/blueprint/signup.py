'''
Handles user creation.
'''

from . import utils, invitation
from ..crypto import hasher
from eve.methods.post import post_internal
from eve.render import _prepare_response
from eve.utils import config
from flask import (
    Blueprint, 
    current_app as app
)

# main blueprint app
blueprint = Blueprint('user_creation', __name__, url_prefix='/signup')

# domain resource
resource = 'user'


@blueprint.route('/resident', methods=['POST'])
def resident_signup():
    '''
    Sign up residents into application.
    '''

    post_insertion = {}

    def add_resident(data):
        data['role'] = ['resident']

    def add_condominium(data):
        token = data.pop('token')
        invite = invitation.find_invite_or_fail(token)
        
        # store it to save later
        post_insertion['invite'] = invite

        # remove condominium
        invite.pop('condominium')

    def on_success():
        invite = post_insertion['invite']

        # remove token
        id_field = config.DOMAIN['invite']['id_field']
        app.data.remove('invite', { id_field: invite['_id'] })

    def add_requirements(data):
        add_resident(data)
        add_condominium(data)

    custom_schema = validation_schema()

    # insert token field
    custom_schema['properties']['token'] = {
        'type': 'string',
    }

    custom_schema['required'].append('token')

    response, status = common_user_creation(add_requirements, 
                                            schema=custom_schema)

    # maybe call on success trigger
    if status == 201:
        on_success()

    return _prepare_response(resource, respose, status=status)


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