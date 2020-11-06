from .domain import load_availables
from eve_sqlalchemy.config import DomainConfig, ResourceConfig

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'postgres://efqoerwldtdzsm:a10ee4a16595b85980eaa2c7dace0c3281170845b12c5496780afb7bad7fafdb@ec2-50-17-197-184.compute-1.amazonaws.com:5432/d51733rsg437ig'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

# The following two lines will output the SQL statements executed by
# SQLAlchemy. This is useful while debugging and in development, but is turned
# off by default.
# --------
SQLALCHEMY_ECHO = True
SQLALCHEMY_RECORD_QUERIES = True

# The default schema is generated using DomainConfig:
DOMAIN = DomainConfig({k: ResourceConfig(v)
                       for k, v in load_availables().items()}).render()