from . import (
    with_auth_user,
    filter_by_auth_user,
    schedule_insertion,
    filter_user_managers,
)

# register modules which contain hooks
modules = [
    with_auth_user,
    filter_by_auth_user,
    schedule_insertion,
    filter_user_managers,
]


def register_all(app):
    for module in modules:
        module.register_hooks(app)