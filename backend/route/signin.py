'''
Handles user authentication.
'''

from flask import request
from eve.utils import config
from eve_auth_jwt import JWTAuth
import jwt

import datetime

INVALID_INPUT = 0
INDETERMINATE_ROLE = 1
UNKNOW_ROLE = 2


def with_fail(code, **kwargs):
    response = {
        'code': code,
        **kwargs
    }

    return (response, 422)


def mount(app):
    '''Entrypoint'''

    @app.route('/signin', methods=['POST'])
    def signin():
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

    def generate_token(user: dict, as_role: str):
        '''
        Generate a new JWT token for user.
        '''

        # get current JWTAuth
        auth = app.auth

        # get token validality
        time_limit = config.JWT_EXP_MINUTES or 60

        expires_in = datetime.datetime.utcnow() + \
                    datetime.timedelta(minutes=time_limit)

        payload = {
            'sub': str(user['_id']),    # account subscriber
            'iss': auth.issuer, # who issued this token
            'exp': expires_in,
            config.JWT_ROLES_CLAIM: [as_role],
        }

        return jwt.encode(payload, auth.secret), expires_in


    def default_auth_failed_response():
        response = {
            'message': 'Invalid credentials',
        }

        return (response, 401)

    def authenticate(email, password, role=None):
        '''
        Try to authenticate given credentials.
        It also gives no implicit information about credentials. 
        '''

        # users domain driver
        users = app.data.driver.db['user']

        # try to find user by email
        found_user = users.find_one({ 'email': email })

        # whether email not in users db
        unknow_user = found_user is None

        # used to store response
        response = None
        
        # when the user does not exists, we fake one
        # why? timing analysis vulnerabilities
        if unknow_user:
            found_user = {
                '_id': 'not matter at all',
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

        # already have a response, send it now
        if response is not None:
            return response

        # authentication failed
        if unknow_user:
            return default_auth_failed_response()
        
        return {
            'accessToken': token,
            'expiresIn': expires_in.timestamp()
        }