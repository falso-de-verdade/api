schema = {
    'name': {
        'required': True,
        'type': 'string',
    },
    'address': {
        'type': 'string',
    },
}


def build_domain():
    return {
        'schema': schema
    }