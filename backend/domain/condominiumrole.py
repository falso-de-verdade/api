#tabela que associa um usuário, com o seu papel (por ex., Maria sendo síndica) com um condomínio
schema = {
    'user': {
        'type': 'objectid',
        'required': True,
        'data_relation': {
            'resource': 'user',
            'field': '_id',
            'embeddable': True,
        },
    },
    'condominium': {    
        'type': 'objectid',
        'required': True,
        'data_relation': {
            'resource': 'condominium',
            'field': '_id',
            'embeddable': True,
        },
    },
    'role': {
        'required': True,
        'type': 'string',
        'allowed': ["resident", "manager"],
    }
}


def build_domain():
    return {
        'schema': schema,
    }