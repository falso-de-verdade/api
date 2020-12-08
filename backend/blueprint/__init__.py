from . import (
    signin,
    signup,
)

# registered routes that mount into application
modules = [
    signin,
    signup,
]


def register_all(app):
    '''
    Register all available blueprints from application context.
    '''

    for module in modules:
        app.register_blueprint(module.blueprint)