schema = {
    'email': {
        'type': 'string',
        'unique': True,
    },
    'name': {
        'type': 'string',
    },
    'pwd_hash': {
        'type': 'string',
    }
}


def build_domain():
    return {
        'schema': schema
    }