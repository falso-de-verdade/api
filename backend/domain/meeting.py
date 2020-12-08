schema = {
    'date': {
        'required': True,
        'type': 'date',
    },
    'fromHour': {
        'required': True,
        'type': 'datetime',
    },
    'toHour': {
        'type': 'datetime',
    },
    'description': {
        'type': 'string',
    },
    'condominiumId': {    
        'required': True,
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