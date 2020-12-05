from . import settings, route
from eve import Eve
from eve_auth_jwt import JWTAuth

import os


def start(mongo_uri, jwt_secret, *args, **kwargs):
    '''
    Start server.
    '''

    app_settings = settings.__dict__
    app_settings['MONGO_URI'] = mongo_uri

    app = Eve(settings=app_settings,
              auth=JWTAuth(secret=jwt_secret))

    # allows custom application routes
    route.register_all(app)
    
    app.run(*args, **kwargs)


def get_settings_path():
    '''
    Get a valid settings file from relative path.
    '''

    abs_path = os.path.dirname(__file__)
    return os.path.join(abs_path, 'settings.py')
