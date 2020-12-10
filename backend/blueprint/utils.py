'''
Helper functions for http parsing.
'''

from eve.utils import config
from eve.methods.common import (
    marshal_write_response,
    build_response_document,
)
from flask import (
    request, 
    abort,
    current_app as app,
)
from flask_cors import CORS
import jsonschema

from functools import wraps


def json_or_fail():
    '''
    Enforce every request to be a JSON payload.
    '''

    if not request.is_json:
        abort(406, 'Content type must be application/json')


def validate_json_request(schema):
    '''
    Parse and validate JSON payload from request.
    '''

    # ensure it is json
    json_or_fail()

    # parse json payload
    payload = request.get_json()

    try:
        jsonschema.validate(payload, schema)
    except jsonschema.ValidationError as e:
        abort(422, e.message)

    # store parsed data based on given properties
    data = {}

    # just grab values from payload
    for key in schema['properties']:
        # add payload value into data when present
        if key in payload:
            data[key] = payload[key]
    return data


def expects_json(schema):
    '''
    Handdy function that automatically validates JSON.
    '''

    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            data = validate_json_request(schema)
            return f(data, *args, **kwargs)
        return wrapper
    return decorator


def cors_from_config(blueprint, config):
    '''
    Apply CORS into blueprint using eve's configuration.
    '''

    kwargs = {
        'origins': config['X_DOMAINS'],
        'allow_headers': config['X_HEADERS'],
    }

    CORS(blueprint, **kwargs)


def build_item_response(resource, _id, save_energy=True):
    '''
    Build response for an item.
    '''

    # grab resource id field
    id_field = config.DOMAIN[resource]['id_field']

    # get user by _id
    document = app.data.find_one_raw(resource, **{ id_field: _id })

    # serialize ObjectId
    document[id_field] = str(document[id_field])

    # build the full response document
    result = document
    build_response_document(result, resource, [], document)

    # add extra write meta data
    result[config.STATUS] = config.STATUS_OK

    if save_energy:
        # limit what actually gets sent to minimize bandwidth usage
        response = marshal_write_response(result, resource)
    else:
        response = result

    return response


def with_error(message, status=422, **kwargs):
    '''
    Helper method for creating responses with error status.
    '''

    # default eve response
    response = {
        '_status': 'ERR',
        '_error': {
            'message': message,
            **kwargs,
        }
    }

    return response, status