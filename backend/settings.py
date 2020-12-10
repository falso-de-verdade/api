from . import domain

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

DOMAIN = domain.load_availables()

# Default JWT configuration
JWT_ROLES_CLAIM = 'roles'
JWT_ISSUER = 'falso-de-verdade_api'

# CORS allowed headers. This configuration is not on documentation
X_HEADERS = [
    'content-type',
    'if-match',
    'authorization',
]

# Disable HATEOS. 
# The web client is not consuming it anyway.
HATEOAS = False

# Minutes which invite links will be valid
# 1 day, by default
INVITE_LIFETIME = 60 * 24