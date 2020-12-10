'''
Module ensure valid condominium removals and clean up.
'''

from ...utils import with_error, id_field
from flask import abort, current_app as app

resource = 'condominium'


def ensure_no_residents(condo_role):
    lookup = {
        resource: condo_role[resource],
        'role': 'resident',
    }
    condos = app.data.find_one_raw('condominiumrole', **lookup)
    if condos:
        response, _ = with_error('Condominium must be empty')
        abort(418, response)


def remove_related_condo(condo_role):
    field = id_field(resource)

    try:
        app.data.remove(resource, { field: condo_role[resource] })
    except:
        app.data.insert('condominiumrole', condo_role)
        raise


def register_hooks(app):
    app.on_delete_item_condominiumrole += ensure_no_residents
    app.on_deleted_item_condominiumrole += remove_related_condo
