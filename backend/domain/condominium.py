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
        'schema': schema,

        # allows only creation and edition
        'resource_methods': ['POST',],
        'item_methods': ['PATCH',],
    }