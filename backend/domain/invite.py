schema = {
    'condominium': {    
        'type': 'objectid',
        'required': True,
        'data_relation': {
            'resource': 'condominium',
            'field': '_id',
            'embeddable': True,
        },
    },
    'token': {
        'required': True,
        'type': 'string',
    },
}


def build_domain():
    return {
        'schema': schema,
        'internal_resource': True,
        'datasource': {
            'aggregation': {
                'pipeline': [
                    {
                        '$lookup': {
                            'from': 'condominium',
                            'localField': 'condominium',
                            'foreignField': '_id',
                            'as': 'condominium',
                        },
                    },
                    {
                        '$match': {
                            '$expr': {
                                '$and': [
                                    {
                                        '$eq': ['$token', '$tokenStr'],
                                    }
                                ]
                            },
                        },
                    },
                ],
            },
        },
    }