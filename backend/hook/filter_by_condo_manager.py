'''
Module provides helper functions to automatically inject
the current authenticated user id into GET lookups.

Usefull for listing and searching for an specific document.
'''

from ..domain.utils import match_auth_user_agg
from eve.methods.get import _perform_aggregation
from eve_auth_jwt import get_request_auth_value
from bson import ObjectId

# resources 
resources = [
    'resident',
]


def filter_by(resource, request, lookup):
    if resource not in resources:
        return

    # pipeline = [
    #     {
    #         '$lookup': {
    #             'from': resource,
    #             'let': { 'condominium': "$condominium" },
    #             'pipeline': [
    #                 {
    #                     '$match': {
    #                         '$expr': {
    #                             '$and': [
    #                                 {
    #                                     '$eq': ["$condominium", "$$condominium"],
    #                                 },
    #                                 {
    #                                     '$eq': ["$role", "manager"],
    #                                 },
    #                             ],
    #                         },
    #                     },
    #                 }
    #             ],
    #             'as': 'clone',
    #         }
    #     },
    #     {
    #         '$match': {
    #             '$and': [
    #                 {
    #                     "role": "resident"
    #                 },
    #             ]
    #         },
    #     },
    #     {
    #         '$unwind': {
    #             'path': "$clone",
    #         },
    #     },
    #     {
    #         '$match': {
    #             '$expr': {
    #                 '$and': [
    #                     {
    #                         '$eq': [
    #                             "$clone.user", 
    #                             ObjectId(get_request_auth_value()),
    #                         ]
    #                     },
    #                 ],
    #             },
    #         },
    #     },
    #     {
    #         '$group': {
    #             '_id': None,
    #             'user': { '$addToSet': "$user" },
    #         },
    #     },
    #     {
    #         '$unwind': {
    #             'path': "$user"
    #         },
    #     },
    # ]

    # response = _perform_aggregation(resource, pipeline, {})
    # print(response)


def register_hooks(app):
    '''
    Entrypoint to inject hook.
    '''

    app.on_pre_GET += filter_by
