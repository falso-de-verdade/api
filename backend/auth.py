from eve.utils import config
from eve_auth_jwt import JWTAuth
import jwt

import datetime


class TokenizerJwtAuth(JWTAuth):
    '''Class to support jwt token authentication and generation'''

    def generate(self, user: dict, as_role: str):
        '''
        Generate a new JWT token for user.
        '''

        # get token validality
        time_limit = config.JWT_EXP_MINUTES or 60

        payload = {
            'sub': user._id,    # account subscriber
            'iss': self.issuer, # who issued this token
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=time_limit),
            config.JWT_ROLES_CLAIM: [as_role],
        }

        return jwt.encode(payload, self.secret)