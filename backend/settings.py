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
JWT_EXP_MINUTES = 60