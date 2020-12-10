schema = {
    'schedule': {    
        'type': 'objectid',
        'required': True,
        'data_relation': {
            'resource': 'schedule',
            'field': '_id',
            'embeddable': True,
        },
    }
}


def build_domain():
    return {
        'schema': schema,
        'embedded_fields': [
            'schedule',
            'schedule.outbuilding',
            'schedule.resident',
        ],
    }