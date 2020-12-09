from . import (
    with_auth_user,
    filter_by_auth_user,
    aggregate_by_auth_user,
)

# register modules which contain hooks
modules = [
    with_auth_user,
    filter_by_auth_user,
    aggregate_by_auth_user,
]


def register_all(app):
    for module in modules:
        module.register_hooks(app)