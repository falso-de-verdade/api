schema = {
    'day': {
        'required': True,
        'type': 'datetime',
    },
    'fromHour': {
        'required': True,
        'type': 'string',
    },
    'toHour': {
        'required': True,
        'type': 'string',
    },
    'occupants': {
        'type': 'integer',
    },
    'pending': {
        'required': True,
        'type': 'boolean',
    },
    'confirmed': {
        'required': True,
        'type': 'boolean',
    },
    'notes': {
        'type': 'string',
    },
    'userId': {    
        'required': True,
        'data_relation': {
            'resource': 'user',
            'field': '_id',
        },
    },
    'outbuildingId': {    
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