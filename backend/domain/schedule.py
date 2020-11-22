schema = {
    'id': {
        'type': 'integer',
        'unique': True,
    },
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
    }
}


def build_domain():
    return {
        'schema': schema
    }