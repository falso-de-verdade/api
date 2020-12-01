schema = {
    'startDate': {
        'type': 'datetime',
    },
    'endDate': {
        'type': 'datetime',
    },
    'startHour': {
        'type': 'string',
    },
    'endHour': {
        'type': 'string',
    }
}


def build_domain():
    return {
        'schema': schema
    }