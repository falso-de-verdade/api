schema = {
    'id': {
        'type': 'integer',
        'unique': True,
    },
    'token_hash': {
        'type': 'string',
    }
}


def build_domain():
    return {
        'schema': schema
    }