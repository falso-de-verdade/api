schema = {
    'schedule_id': {    
        'required': True,
        'data_relation': {
            'resource': 'schedule',
            'field': '_id',
        },
    }
}


def build_domain():
    return {
        'schema': schema
    }