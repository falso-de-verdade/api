from eve.utils import config

from secrets import token_hex
from datetime import date

hour_re = r'^([0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$'


def coerce_date(date_str):
    '''
    Transforms a date string into an ISO format.
    '''

    date_obj = date.fromisoformat(date_str)
    return date_obj.isoformat()


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