schema = {
    'id': {
        'type': 'integer',
        'unique': True,
    },
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