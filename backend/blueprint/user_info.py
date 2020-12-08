'''
Handles user default resource for self information.
'''

from . import utils
from ..crypto import hasher
from flask import Blueprint, current_app as app
from eve_auth_jwt import (
    requires_token,
    get_request_auth_value,
    get_authen_roles,
)

# main blueprint app
blueprint = Blueprint('user_info', __name__)


@blueprint.route('/user/me', methods=['GET'])
@requires_token()
def me():
    '''
    Return information of current logged user.
    '''

    # get user id from token
    account_id = get_request_auth_value()

    # build full response for user
    response = utils.build_item_response('user', 
                                         account_id, 
                                         save_energy=False)

    # helper attribute for client
    response['isManager'] = get_authen_roles() == ['manager']

    return response, 200