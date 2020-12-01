schema = {
    'date': {
        'type': 'date',
    },
    'startHour': {
        'type': 'string',
    },
    'duration': {
        'type': 'string',
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