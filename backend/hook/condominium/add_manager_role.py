'''
Module add a condominium role for manager on created condominiums.
'''

from ... import utils
from eve.methods.post import post_internal
from eve_auth_jwt import get_request_auth_value
from flask import current_app as app

resource = 'condominium'


def id_field():
    return utils.id_field(resource)


def create_role(condominium):
    payload = {
        'condominium': condominium[id_field()],
        'user': get_request_auth_value(),
        'role': 'manager',
    }
    response, _, _, status, _ = post_internal('condominiumrole', payl=payload)
    if status != 201:
        raise Exception('Error when creating condominium role for manager')


def create_role_or_rollback(items):
    field = id_field()
    for condominium in items:
        try:
            create_role(condominium)
        except:
            app.data.remove(resource, { field: condominium[field] })
            raise


def register_hooks(app):
    app.on_inserted_condominium += create_role_or_rollback