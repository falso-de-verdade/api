'''
Module provides helper functions to automatically inject
the current authenticated user id into GET lookups.

Usefull for listing and searching for an specific document.
'''

from .utils import handle_resources_auth_user

# resources 
resources = [
    'condominiumrole',
    'outbuilding',
    'schedule',
]

# resources protected when user is resident
resident_resources = [
    'schedule',
]


def on_resident(user_id, _, lookup):
    lookup['resident'] = user_id


def on_manager(user_id, _, lookup):
    lookup['user'] = user_id


def register_hooks(app):
    '''
    Entrypoint to inject hook.
    '''

    handler = handle_resources_auth_user(on_resident,
                                         on_manager,
                                         resident_resources,
                                         resources)
    app.on_pre_GET = handler
