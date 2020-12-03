schema = {
    'date': {
        'type': 'date',
    },
    'fromHour': {
        'type': 'datetime',
    },
    'toHour': {
        'type': 'datetime',
    },
    'description': {
        'type': 'string',
    },
    'condominiumId': {    
        # 'required': True,
        'data_relation': {
            'resource': 'condominium',
            'field': '_id',
        },
    },
}


def build_domain():
    return {
        'schema': schema
    }