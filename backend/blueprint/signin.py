'''
Handles user authentication.
'''

from ..crypto import hasher, generate_token
from flask import (
    Blueprint, 
    request, 
    current_app as app
)

INVALID_INPUT = 0
INDETERMINATE_ROLE = 1
UNKNOW_ROLE = 2

# main blueprint app
blueprint = Blueprint('authentication', __name__)


@blueprint.route('/signin', methods=['POST'])
def signin():
    '''
    Sign users into application.
    '''

    # enfore JSON
    if not request.is_json:
        return ('Content type must be application/json', 406)

    # parse data, get dict
    data = request.get_json(cache=False)

    # store missing fields
    missing = []
    email, password, role = data.get('email'), data.get('password'), data.get('role')

    # validate input
    if not email:
        missing.append(email)
    elif not password:
        missing.append(password)

    # validation failed
    if missing:
        return with_fail(INVALID_INPUT, missing=missing)

    return authenticate(email, password, role)


def with_fail(code, **kwargs):
    '''
    Helper method for creating responses with error status.
    '''

    response = {
        'code': code,
        **kwargs
    }

    return (response, 422)


def users():
    '''
    Users DB domain driver.
    '''

    return app.data.driver.db['user']


def default_auth_failed_response():
    '''
    Default response for failed authentications.
    '''

    response = {
        'message': 'Invalid credentials',
    }

    return (response, 401)


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
        new_hash = hasher.hash(passwd_str)

        # update users password with new hash
        users().update({ '_id': user['_id'] },
                        { '$set': { 'passwdHash': new_hash } })

    return True
            

def authenticate(email, password, role=None):
    '''
    Try to authenticate given credentials.
    It also gives no implicit information about credentials. 
    '''

    # try to find user by email
    found_user = users().find_one({ 'email': email })

    # whether email not in users db
    unknow_user = found_user is None

    # used to store response
    response = None
    
    # when the user does not exists, we fake one
    # why? timing analysis vulnerabilities
    if unknow_user:
        found_user = {
            '_id': 'not matter at all',
            'passwordHash': '$argon2id$v=19$m=102400,t=2,p=8$OK35XzsioyZ9J5K/l+nHxg$eRpQ1rH8D+JTfmbdmT+psw',
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
                response = with_fail(INDETERMINATE_ROLE,
                                     message=message)

        elif role not in user_roles:
            message = f'Unknow role: {role}'
            response = with_fail(UNKNOW_ROLE, message=message)

    # generate a new jwt token for user
    token, expires_in = generate_token(found_user, role)

    # check whether password is ok
    isPasswdOk = verify_user_passwd(password, found_user)

    # already have a response, send it now
    if response is not None:
        return response

    # authentication failed
    if not isPasswdOk or unknow_user:
        return default_auth_failed_response()
    
    return {
        'accessToken': token,
        'expiresIn': expires_in.timestamp()
    }