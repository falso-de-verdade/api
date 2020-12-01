#tabela associativa que liga todos os agendamentos rejeitados com o mesmo
#conflito
schema = {
    'collisionId': {    
        'required': True,
        'data_relation': {
            'resource': 'collision',
            'field': '_id',
        },
    },
    'scheduleId': {    
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