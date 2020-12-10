'''
Handles user default resource for self information.
'''

from . import utils
from ..crypto.token import random_urlsafe_token
from eve.utils import config
from eve_auth_jwt import requires_token, get_authen_roles
from flask import (
    Blueprint,
    current_app as app,
)

# main blueprint app
blueprint = Blueprint('invitation', __name__)

validation_schema = {
    'type': 'object',
    'properties': {
        'condominium': {
            'type': 'string',
        },
    },
    'required': [
        'condominium',
    ],
}

@blueprint.route('/invite', methods=['POST'])
@requires_token(allowed_roles=['manager'])
@utils.expects_json(validation_schema)
def generate_invite(content):
    '''
    Generate an invitation link to join condominium.
    '''

    content['token'] = random_urlsafe_token()
    app.data.insert('invite', content)

    host = config.CLIENT_HOST.lstrip('/')
    link = f'{host}/invite/{content["token"]}'

    return {
        'link': link,
    }