schema = {
    'tokenHash': {
        'type': 'string',
    },
    'userId': {    
        # 'required': True,
        'data_relation': {
            'resource': 'user',
            'field': '_id',
        },
    }
}


def build_domain():
    return {
        'schema': schema
    }