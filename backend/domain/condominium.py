schema = {
    'name': {
        'required': True,
        'type': 'string',
    },
    'address': {
        'type': 'string',
    },
    'user': {
        'type': 'objectid',
        'required': True,
        'data_relation': {
            'resource': 'user',
            'field': '_id',
            'embeddable': True,
        },
    }
}


def build_domain():
    return {
        'schema': schema
    }