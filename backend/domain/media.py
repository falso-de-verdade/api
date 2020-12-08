schema = {
    'name': {
        'required': True,
        'type': 'string',
    },
    'path': {
        'required': True,
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