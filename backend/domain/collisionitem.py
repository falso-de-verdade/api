#tabela associativa que liga todos os agendamentos rejeitados com o mesmo
#conflito
schema = {
    'collision': {    
        'type': 'objectid',
        'required': True,
        'data_relation': {
            'resource': 'collision',
            'field': '_id',
            'embeddable': True,
        },
    },
    'scheduleId': {    
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
        'schema': schema
    }