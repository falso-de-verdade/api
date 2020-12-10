'''
Handles user default resource for self information.
'''

from . import utils
from ..crypto.token import random_urlsafe_token
from eve.methods.post import post_internal
from eve.methods.get import get_internal
from eve.utils import config
from eve.render import _prepare_response
from eve_auth_jwt import requires_token, get_authen_roles
from flask import (
    Blueprint,
    request,
    abort,
    current_app as app,
)

from datetime import timedelta, datetime, timezone

# main blueprint app
blueprint = Blueprint('invitation', __name__)

resource = 'invite'

invite_creation_schema = {
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
@utils.expects_json(invite_creation_schema)
def generate_invite(content):
    '''
    Generate an invitation link to join condominium.
    '''

    content['token'] = random_urlsafe_token()
    post_internal('invite', payl=content)

    host = config.CLIENT_HOST.lstrip('/')
    link = f'{host}/invite/{content["token"]}'

    return {
        'link': link,
    }


@blueprint.route('/invite/<token>', methods=['GET'])
def lookup_invite(token):
    '''
    Invite lookup by token.
    '''

    # patch request with aggregation data
    request.args = {
        'aggregate': f'{{"$tokenStr":"{token}"}}',
        'max_results': 1,
    }

    # find invite using aggregation
    content, _, _, status, _ = get_internal(resource)
    if not content['_items']:
        on_invalid_token()

    response = content['_items'][0]
    response['condominium'] = response['condominium'][0]
    return _prepare_response(resource, response, status=status)



def find_invite_or_fail(token):
    '''
    Try to find an invite from invite token.
    '''

    invite = app.data.find_one_raw(resource, **{ 'token': token })
    validate_invite(invite)
    return invite


def validate_invite(invite):
    '''
    Abort whether invite is no longer valid
    '''

    # ensure token exists
    if invite is None:
        on_invalid_token()

    # calculate how many time has gone
    elapsed = datetime.now(timezone.utc) - invite['_created']

    if elapsed > timedelta(minutes=config.INVITE_LIFETIME):
        on_invalid_token()


def on_invalid_token():
    abort(422, 'Unknow token')