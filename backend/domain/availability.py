schema = {
    'start_date': {
        'type': 'datetime',
    },
    'end_date': {
        'type': 'datetime',
    },
    'start_hour': {
        'type': 'string',
    },
    'end_hour': {
        'type': 'string',
    }
}


def build_domain():
    return {
        'schema': schema
    }