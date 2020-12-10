schema = {
    'schedule': {    
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
        'schema': schema,
        # 'datasource': {
        #     'aggregation': {
        #         'pipeline': [
        #             {
        #                 '$lookup': {
        #                     'from': 'collisionitem',
        #                     'localField': '_id',
        #                     'foreignField': 'collision',
        #                     'as': as_,
        #                 },
        #             },
        #         ]
        #     }
        # }   
    }