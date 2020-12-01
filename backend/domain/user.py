schema = {
    'email': {
        'type': 'string',
        'unique': True,
    },
    'name': {
        'type': 'string',
    },
    'pwdHash': {
        'type': 'string',
    },
    'role': {
        'type': 'list',
        'allowed': ["resident", "manager"],
    }
}


def build_domain():
    return {
        'schema': schema
    }