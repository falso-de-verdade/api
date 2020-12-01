#tabela associativa que liga todos os agendamentos rejeitados com o mesmo
#conflito
schema = {
    'collision_id': {    
        'required': True,
        'data_relation': {
            'resource': 'collision',
            'field': '_id',
        },
    },
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