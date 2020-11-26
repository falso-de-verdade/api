schema = {
    'name': {
        'type': 'string',
    },
    'description': {
        'type': 'string',
    },
    'capacity': {
        'type': 'integer',
    }
}


def build_domain():
    return {
        'schema': schema
    }