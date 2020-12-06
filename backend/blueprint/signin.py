'''
Handles user authentication.
'''

from . import utils
from ..crypto import hasher, generate_token
from eve.utils import config
from flask import (
    Blueprint, 
    current_app as app
)

INDETERMINATE_ROLE = 0
UNKNOW_ROLE = 1

# main blueprint app
blueprint = Blueprint('authentication', __name__)

# domain used in this blueprint
resource = 'user'

validation_schema = {
    'type': 'object',
    'properties': {
        'email': {
            'type': 'string',
        },
        'password': {
            'type': 'string',
        },
        'role': {
            'type': 'string',
            'enum': ['resident', 'manager',],
        },
    },
    'required': [
        'email',
        'password',
    ],
}


@blueprint.route('/signin', methods=['POST'])
@utils.expects_json(validation_schema)
def signin(data):
    '''
    Sign users into application.
    '''

    # required fields
    email, password = data['email'], data['password']

    # optional field
    role = data.get('role') 

    return authenticate(email, password, role)


def with_fail(message, status=422, **kwargs):
    '''
    Helper method for creating responses with error status.
    '''

    # default eve response
    response = {
        '_status': 'ERR',
        '_error': {
            'message': message,
            **kwargs,
        }
    }

    return response, status


def default_auth_failed_response():
    '''
    Default response for failed authentications.
    '''

    return with_fail('Invalid credentials',
                     status=401)


def verify_user_passwd(passwd_str: str, user: dict):
    '''
    Verify the password against the user.
    '''

    # grab the user password
    passwd_hash = user['passwdHash']

    if not hasher.verify(passwd_hash, passwd_str):
        return False

    # check whether password hash should be rehashed
    if hasher.needs_rehash(passwd_hash):
        # recalculate password hash
        new_hash = hasher.hash(passwd_str)

        # default domain id
        id_field = config.DOMAIN[resource]['id_field']

        # update users password with new hash
        # we are using the raw driver call to avoid
        # eve's etag constraints
        raw_driver().update({ id_field: user[id_field] },
                            { '$set': { 'passwdHash': new_hash } })

    return True


def raw_driver():
    '''
    Domain database driver.
    '''

    return app.data.driver.db[resource]
            

def authenticate(email, password, role=None):
    '''
    Try to authenticate given credentials.
    It also gives no implicit information about credentials. 
    '''

    # try to find user by email
    found_user = raw_driver().find_one({ 'email': email })

    # whether email not in users db
    unknow_user = found_user is None

    # used to store response
    response = None
    
    # when the user does not exists, we fake one
    # why? timing analysis vulnerabilities
    if unknow_user:
        # default domain id
        id_field = config.DOMAIN[resource]['id_field']

        found_user = {
            id_field: 'not matter at all',
            'passwdHash': '$argon2id$v=19$m=102400,t=2,p=8$OK35XzsioyZ9J5K/l+nHxg$eRpQ1rH8D+JTfmbdmT+psw',
        }
    else:
        # get all user roles
        user_roles = found_user['role']

        # can we pick a role by ourselves
        if not role:
            if len(user_roles) == 1:
                role = user_roles[0]
            else:
                message = 'Re-send the request with a {role} field'

                # unfortunately we can not proceed
                # user must send another request with 
                # a role of choice
                response = with_fail(message,
                                     code=INDETERMINATE_ROLE)

        elif role not in user_roles:
            message = f'Unknow role: {role}'
            response = with_fail(message,
                                 code=UNKNOW_ROLE)

    # generate a new jwt token for user
    token, expires_in = generate_token(found_user, role)

    # check whether password is ok
    is_passwd_ok = verify_user_passwd(password, found_user)

    # already have a response, send it now
    if response is not None:
        return response

    # authentication failed
    if not is_passwd_ok or unknow_user:
        return default_auth_failed_response()
    
    return {
        'accessToken': token,
        'expiresIn': expires_in.timestamp()
    }