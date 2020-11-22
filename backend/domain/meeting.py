schema = {
    'id': {
        'type': 'integer',
        'unique': True,
    },
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
    }
}


def build_domain():
    return {
        'schema': schema
    }