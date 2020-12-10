from .utils import hour_re, coerce_date

schema = {
    'day': {
        'required': True,
        'type': 'string',
        'coerce': coerce_date,
    },
    'fromHour': {
        'required': True,
        'type': 'string',
        'regex': hour_re,
    },
    'toHour': {
        'required': True,
        'type': 'string',
        'regex': hour_re,
    },
    'occupants': {
        'type': 'integer',
    },

    # enforced by hook
    'confirmed': {
        'type': 'boolean',
    },
    'notes': {
        'type': 'string',
    },
    'resident': {    
        'type': 'objectid',
        'required': True,
        'data_relation': {
            'resource': 'user',
            'field': '_id',
            'embeddable': True,
        },
    },
    'outbuilding': {    
        'type': 'objectid',
        'required': True,
        'data_relation': {
            'resource': 'outbuilding',
            'field': '_id',
            'embeddable': True,
        },
    },
    # manager user, not required because will be 
    # enforced by a hook
    'user': {    
        'type': 'objectid',
        'data_relation': {
            'resource': 'user',
            'field': '_id',
        },
    },
}


def build_domain():
    return {
        'schema': schema,
    }