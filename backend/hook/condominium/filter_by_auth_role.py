'''
Module add a filter lookup to filter by authenticated user role.
'''

from eve_auth_jwt import get_authen_roles


def inject_role_from_auth(request, lookup):
    lookup['role'] = get_authen_roles()[0]


def register_hooks(app):
    app.on_pre_GET_condominiumrole += inject_role_from_auth