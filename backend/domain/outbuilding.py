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
    'condominiumId': {    
        # 'required': True,
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