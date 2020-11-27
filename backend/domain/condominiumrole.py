#tabela que associa um papel de usuário (por ex., Maria sendo síndica) com um condomínio
schema = {
    'user_id': {    
        'required': True,
        'data_relation': {
            'resource': 'user',
            'field': '_id',
        },
    },
    'condominium_id': {    
        'required': True,
        'data_relation': {
            'resource': 'condominium',
            'field': '_id',
        },
    },
    'role': {
        'type': 'list',
        'allowed': ["resident", "manager"],
    }
}


def build_domain():
    return {
        'schema': schema
    }