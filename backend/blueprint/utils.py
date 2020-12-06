'''
Helper functions for http parsing.
'''

from functools import wraps
from flask import (
    request, 
    abort,
)
import jsonschema


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