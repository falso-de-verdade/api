from .domain.util import Base
from . import settings
from eve import Eve
from eve_sqlalchemy import SQL
from eve_sqlalchemy.validation import ValidatorSQL

import os


def start():
    '''
    Start server.
    '''

    app = Eve(settings=settings.__dict__, 
              validator=ValidatorSQL, 
              data=SQL)

    setup_db(app)

    app.run()


def setup_db(app: Eve):
    '''
    Setup database into eve application instance.
    '''

    db = app.data.driver
    Base.metadata.bind = db.engine
    db.Model = Base
    db.create_all()


def get_settings_path():
    '''
    Get a valid settings file from relative path.
    '''

    abs_path = os.path.dirname(__file__)
    return os.path.join(abs_path, 'settings.py')
