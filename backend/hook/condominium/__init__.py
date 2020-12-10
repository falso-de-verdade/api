from . import (
    add_manager_role,
    filter_by_auth_role,
    handle_removal,
)

# register modules which contain hooks
modules = [
    add_manager_role,
    filter_by_auth_role,
    handle_removal,
]


def register_hooks(app):
    for module in modules:
        module.register_hooks(app)