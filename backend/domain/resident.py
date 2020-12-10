from . condominiumrole import schema


def build_domain():
    return {
        'schema': schema,

        'datasource': {
            'source': 'condominiumrole',
        },

        # only manager
        'allowed_roles': ['manager'],

        'embedded_fields': [
            'user',
        ]
    }