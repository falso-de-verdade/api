from . import settings
from eve import Eve

import os


def start():
    '''
    Start server.
    '''

    app = Eve(settings=settings.__dict__)
    app.run()


def get_settings_path():
    '''
    Get a valid settings file from relative path.
    '''

    abs_path = os.path.dirname(__file__)
    return os.path.join(abs_path, 'settings.py')
