schema = {
    'name': {
        'type': 'string',
    },
    'description': {
        'type': 'string',
    },
    'capacity': {
        'type': 'integer',
    },
    'condominium_id': {    
        'required': True,
        'data_relation': {
            'resource': 'condominium',
            'field': '_id',
        },
    },
}


def build_domain():
    return {
        'schema': schema
    }