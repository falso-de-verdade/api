from eve.utils import config
from eve_auth_jwt import get_authen_roles


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


def is_manager():
    return 'manager' in get_authen_roles()