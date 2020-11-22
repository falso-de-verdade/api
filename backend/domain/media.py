schema = {
    'id': {
        'type': 'integer',
        'unique': True,
    },
    'name': {
        'type': 'string',
    },
    'path': {
        'type': 'string',
    }
}


def build_domain():
    return {
        'schema': schema
    }