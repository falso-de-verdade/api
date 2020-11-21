import backend.app
from dotenv import load_dotenv

import os


def main():
    # maybe load environment variables in runtime
    if os.path.exists('.env'):
        load_dotenv()

    # MongoDB database connection
    mongo_uri = os.getenv('MONGO_URI')

    assert mongo_uri, 'Missing MONGO_URI database connection uri'

    # get server info
    host = os.getenv('HOST') or None
    port = os.getenv('PORT') or None

    # Logging verbosity
    debug = os.getenv('DEBUG') == '1'

    backend.app.start(mongo_uri=mongo_uri,
                      host=host, 
                      port=port,
                      debug=debug)


if __name__ == '__main__':
    main()