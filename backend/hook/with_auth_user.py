'''
Module provides helper functions to automatically inject
the current authenticated user id into POST payload data.

Usefull for creation.
'''

from .utils import handle_resources_auth_user

# resources 
resources = [
    'condominium',
    'outbuilding',
]

# resources that contains a resident user 
resident_resources = [
    'schedule',
]


def on_resident(user_id, request, *args):
    request.json['resident'] = user_id


def on_manager(user_id, request, *args):
    request.json['user'] = user_id


def register_hooks(app):
    '''
    Entrypoint to inject hook.
    '''

    handler = handle_resources_auth_user(on_resident,
                                         on_manager,
                                         resident_resources,
                                         resources)
    app.on_pre_POST = handler
