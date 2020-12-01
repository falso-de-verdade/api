schema = {
    'name': {
        'type': 'string',
    },
    'path': {
        'type': 'string',
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