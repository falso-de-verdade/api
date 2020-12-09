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