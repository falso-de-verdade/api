'''
Module provides helper functions to automatically inject
the current authenticated user id into aggregation pipelines.

Usefull for restricting access on listings.
'''

from eve_auth_jwt import get_request_auth_value
from bson import ObjectId

resources = [
    'outbuilding',
] 


def inject_agg_user_id(resource, pipeline):
    '''
    Inject userId into aggregation pipeline.
    '''

    if resource not in resources:
        return

    match_index = None

    # try to find the index of "$match" stage
    for index, stages in enumerate(pipeline):
        if '$match' in stages:
            match_index = index 
            break        
    
    if match_index is None:
        return

    _id = ObjectId(get_request_auth_value())

    # overwrite compare sequence to user id
    pipeline[match_index]['$match']['$expr']['$eq'][1] = _id


def register_hooks(app):
    '''
    Entrypoint to inject hook.
    '''

    app.before_aggregation = inject_agg_user_id
