from . import settings
from eve import Eve

import os


def start(mongo_uri, *args, **kwargs):
    '''
    Start server.
    '''

    app_settings = settings.__dict__
    app_settings['MONGO_URI'] = mongo_uri

    app = Eve(settings=app_settings)
    app.run(*args, **kwargs)


def get_settings_path():
    '''
    Get a valid settings file from relative path.
    '''

    abs_path = os.path.dirname(__file__)
    return os.path.join(abs_path, 'settings.py')
