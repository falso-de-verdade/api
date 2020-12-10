schema = {
    'condominium': {
        'required': True,
        'type': 'string',
    },
    'token': {
        'required': True,
        'type': 'string',
    },
}


def build_domain():
    return {
        'schema': schema,
        'internal_resource': True,
    }