schema = {
    'email': {
        'type': 'string',
        'unique': True,
    },
    'name': {
        'type': 'string',
    },
    'passwdHash': {
        'type': 'string',
    },
    'location': {
        'type': 'string',
    },
    'role': {
        'type': 'list',
        'allowed': ["resident", "manager"],
    }
}


def build_domain():
    return {
        'schema': schema,

        # override to only allow listing users
        # user creation is done by signup route
        'resource_methods': ['GET',],
    }