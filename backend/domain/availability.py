schema = {
    'fromDay': {
        'required': True,
        'type': 'integer',
    },
    'toDay': {
        'required': True,
        'type': 'integer',
    },
    'fromHour': {
        'required': True,
        'type': 'string',
    },
    'toHour': {
        'required': True,
        'type': 'string',
    }
}


def build_domain():
    return {
        'schema': schema
    }