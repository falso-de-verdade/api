from eve.utils import config

from secrets import token_hex


def match_auth_user_agg(from_, 
                        local_field=None, 
                        foreign_field=None,
                        name=None):
    '''
    Create an aggregation pipeline to match the user 
    id from a foreign document.
    '''

    local_field = local_field or from_
    foreign_field = foreign_field or config.ID_FIELD
    as_ = name or f'{from_}-{token_hex(3)}' 
    
    return [
        {
            '$lookup': {
                'from': from_,
                'localField': local_field,
                'foreignField': foreign_field,
                'as': as_,
            },
        },
        {
            '$unwind': {
                'path': f'${as_}',
            },
        },
        {
            '$match': {
                '$expr': {
                    '$eq': [
                        f'${as_}.user', 
                        'will-be-replaced',
                    ],
                },
            },
        },
    ]