from .utils import hour_re

schema = {
    'name': {
        'required': True,
        'type': 'string',
    },
    'description': {
        'type': 'string',
    },
    'capacity': {
        'required': True,
        'type': 'integer',
    },
    'availabilities': {
        'type': 'list',
        'minlength': 1,
        'schema': {
            'type': 'dict',
            'schema': {
                'fromDay': {
                    'required': True,
                    'type': 'integer',
                    'allowed': range(0, 6),
                },
                'toDay': {
                    'type': 'integer',
                    'allowed': range(-1, 6),
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
            },
        },
    },
    'condominium': {    
        'type': 'objectid',
        'required': True,
        'data_relation': {
            'resource': 'condominium',
            'field': '_id',
            'embeddable': True,
        },
    },
    'user': {    
        'type': 'objectid',
        'required': True,
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