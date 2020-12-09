from . import settings, blueprint, hook
from eve import Eve
from eve_auth_jwt import JWTAuth

import os


def start(settings_override,
          *args, 
          **kwargs):
    '''
    Start server.
    '''

    app_settings = settings.__dict__
    app_settings.update(settings_override)

    app = Eve(settings=app_settings,
              auth=JWTAuth)

    # allows custom data handling
    hook.register_all(app)

    # allows custom application routes
    blueprint.register_all(app)

    app.run(*args, **kwargs)


def get_settings_path():
    '''
    Get a valid settings file from relative path.
    '''

    abs_path = os.path.dirname(__file__)
    return os.path.join(abs_path, 'settings.py')
