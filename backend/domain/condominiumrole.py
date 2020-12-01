#tabela que associa um usuário, com o seu papel (por ex., Maria sendo síndica) com um condomínio
schema = {
    'userId': {    
        'required': True,
        'data_relation': {
            'resource': 'user',
            'field': '_id',
        },
    },
    'condominiumId': {    
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