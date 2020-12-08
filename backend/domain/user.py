schema = {
    'email': {
        'required': True,
        'type': 'string',
        'unique': True,
    },
    'name': {
        'required': True,
        'type': 'string',
    },
    'passwdHash': {
        'required': True,
        'type': 'string',
    },
    'location': {
        'type': 'string',
    },
    'role': {
        'required': True,
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