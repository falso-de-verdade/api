'''
Module add a filter lookup to find users who the
logged user manages.
'''

from eve_auth_jwt import get_request_auth_value


def on_internal_find(request, lookup):
    lookup['managers'] = {
        '$in': [get_request_auth_value()]
    }
    lookup['role'] = {
        '$eq': ['resident'],
    }


def register_hooks(app):
    app.on_pre_GET_user += on_internal_find