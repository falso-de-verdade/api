schema = {
    'id': {
        'type': 'integer',
        'unique': True,
    },
    'name': {
        'type': 'string',
    },
    'address': {
        'type': 'string',
    }
}


def build_domain():
    return {
        'schema': schema
    }