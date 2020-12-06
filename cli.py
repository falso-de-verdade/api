import backend.app
from dotenv import load_dotenv

import os

# environment variables required to start application
req_variables = [
    'MONGO_URI',
    'JWT_SECRET',
]

# other variables searched, but not required
non_req_variables = [
    'JWT_EXP_MINUTES',
]


def main():
    # maybe load environment variables in runtime
    if os.path.exists('.env'):
        load_dotenv()

    # load application params
    parameters = load_env_parameters()

    # ensure expiration is an python integer
    if parameters['jwt_exp_minutes']:
        try:
            expiration = int(parameters['jwt_exp_minutes'])
        except ValueError:
            print('[ERROR] Environment JWT_EXP_MINUTES must be an integer.')
            return

        parameters['jwt_exp_minutes'] = expiration

    # get server info
    host = os.getenv('HOST') or None
    port = os.getenv('PORT') or None

    # Logging verbosity
    debug = os.getenv('DEBUG') == '1'

    backend.app.start(host=host, 
                      port=port,
                      debug=debug,
                      **parameters)


def load_env_parameters():
    '''
    Load main parameters to start application.
    '''

    parameters = {}

    def load_and_maybe_ensure(name, ensure=True):
        '''
        Helper function to add parameter from system environment
        and maybe ensure it's value is not missing.
        '''

        value = os.getenv(name)
        if ensure:
            assert value, f'Missing environment var: {name}' 
        parameters[name.lower()] = value

    for name in req_variables:
        load_and_maybe_ensure(name)

    for name in non_req_variables:
        load_and_maybe_ensure(name, ensure=False)

    return parameters


if __name__ == '__main__':
    main()