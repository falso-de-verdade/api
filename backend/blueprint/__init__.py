from . import (
    utils,
    signin,
    signup,
    user_info,
    invitation,
)

# registered routes that mount into application
modules = [
    signin,
    signup,
    user_info,
    invitation,
]


def register_all(app):
    '''
    Register all available blueprints from application context.
    '''

    for module in modules:
        blueprint = module.blueprint

        # apply cors settings
        utils.cors_from_config(blueprint, app.settings)

        # finally register blueprint
        app.register_blueprint(blueprint)
