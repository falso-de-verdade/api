from eve.utils import config
from flask import current_app as app
import jwt

from base64 import b64encode
from secrets import token_urlsafe
import datetime


def generate_token(user: dict, as_role: str):
    '''
    Generate a new JWT token for user.
    '''

    # get token validality
    time_limit = config.JWT_EXP_MINUTES or 60

    expires_in = datetime.datetime.utcnow() + \
                 datetime.timedelta(minutes=time_limit)

    payload = {
        'sub': str(user['_id']),    # account subscriber
        'iss': app.auth.issuer,   # who issued this token
        'exp': expires_in,
        config.JWT_ROLES_CLAIM: [as_role],
    }

    return jwt.encode(payload, app.auth.secret), expires_in


def random_urlsafe_token():
    '''
    Generate PSRNG tokens.
    '''

    return token_urlsafe(64)