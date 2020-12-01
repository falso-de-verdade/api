schema = {
    'name': {
        'type': 'string',
    },
    'path': {
        'type': 'string',
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