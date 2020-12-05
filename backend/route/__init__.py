from . import (
    signin,
)

# registered routes that mount into application
routes = [
    signin,
]


def register_all(app):
    '''
    Register all available routes from application context.
    '''

    for module in routes:
        module.mount(app)