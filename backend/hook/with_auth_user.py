'''
Module provides helper functions to automatically inject
the current authenticated user id into POST payload data.

Usefull for creation.
'''

from eve_auth_jwt import get_request_auth_value

# resources 
resources = [
    'condominium',
]


def on_internal_creations(resource, request, *args):
    '''
    Inject userId into payload.
    '''

    if resource in resources:
        request.json['user'] = get_request_auth_value()


def register_hooks(app):
    '''
    Entrypoint to inject hook.
    '''

    app.on_pre_POST = on_internal_creations
