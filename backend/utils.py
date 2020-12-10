from eve.utils import config


def id_field(resource):
    '''
    Default id field for domain.
    '''

    return config.DOMAIN[resource]['id_field']


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