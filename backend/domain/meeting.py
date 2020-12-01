schema = {
    'date': {
        'type': 'datetime',
    },
    'start_hour': {
        'type': 'string',
    },
    'duration': {
        'type': 'string',
    },
    'description': {
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