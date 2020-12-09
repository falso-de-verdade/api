from .utils import match_auth_user_agg

schema = {
    'name': {
        'required': True,
        'type': 'string',
    },
    'description': {
        'type': 'string',
    },
    'capacity': {
        'required': True,
        'type': 'integer',
    },
    'condominium': {    
        'type': 'objectid',
        'required': True,
        'data_relation': {
            'resource': 'condominium',
            'field': '_id',
            'embeddable': True,
        },
    },
}


def build_domain():
    return {
        'schema': schema,

        'datasource': {
            'aggregation': {
                'pipeline': match_auth_user_agg('condominium'),
            }
        }
    }