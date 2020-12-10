from . import (
    with_auth_user,
    filter_by_auth_user,
    schedule_insertion,
    filter_users,
    filter_by_auth_role,
    condominium,
)

# register modules which contain hooks
modules = [
    with_auth_user,
    filter_by_auth_user,
    schedule_insertion,
    filter_users,
    filter_by_auth_role,
    condominium,
]


def register_all(app):
    for module in modules:
        module.register_hooks(app)