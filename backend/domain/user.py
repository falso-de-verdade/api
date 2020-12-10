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
    },

    # list of user ids
    'managers': {
        'type': 'list',
        'schema': {
            'type': 'objectid',
        },
        'readonly': True,
    }
}


def build_domain():
    return {
        'schema': schema,

        # override to only allow listing users
        # user creation is done by signup route
        'resource_methods': ['GET',],

        # project all but passwdHash, which is sensitive
        'datasource': {
            'filter': {
                'role': {
                    '$eq': ['resident'],
                },
            },

            'projection': {
                'email': 1,
                'name': 1,
                'location': 1,
            },
        },
    }