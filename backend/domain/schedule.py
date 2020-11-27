schema = {
    'day': {
        'type': 'datetime',
    },
    'start_hour': {
        'type': 'string',
    },
    'end_hour': {
        'type': 'string',
    },
    'occupants': {
        'type': 'integer',
    },
    'pending': {
        'type': 'boolean',
    },
    'confirmed': {
        'type': 'boolean',
    },
    'user_id': {    
        'required': True,
        'data_relation': {
            'resource': 'user',
            'field': '_id',
        },
    },
    'outbuilding_id': {    
        'required': True,
        'data_relation': {
            'resource': 'outbuilding',
            'field': '_id',
        },
    }
}


def build_domain():
    return {
        'schema': schema
    }