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
    'condominiumId': {    
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