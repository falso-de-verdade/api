schema = {
    'fromDay': {
        'type': 'integer',
    },
    'toDay': {
        'type': 'integer',
    },
    'fromHour': {
        'type': 'string',
    },
    'toHour': {
        'type': 'string',
    }
}


def build_domain():
    return {
        'schema': schema
    }