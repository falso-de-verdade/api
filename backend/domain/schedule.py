schema = {
    'day': {
        'type': 'datetime',
    },
    'startHour': {
        'type': 'string',
    },
    'endHour': {
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