from . import (
    user, passwordreset, condominium,
    schedule, meeting, outbuilding,
    availability, media, collision, collisionitem,
    condominiumrole
)


# Registered modules which contains information about a domain.
modules = {
    'user': user,
    'passwordreset': passwordreset,
    'condominium': condominium,
    'schedule': schedule,
    'meeting': meeting,
    'outbuilding': outbuilding,
    'availability': availability,
    'media': media,
    'collision': collision,
    'collisionitem': collisionitem,
    'condominiumrole': condominiumrole
}


def load_availables():
    '''Load all available domains.'''

    domains = {}
    for name, module in modules.items():
        domain = parse_domain(module)
        domains[name] = domain
    return domains


def parse_domain(module: list):
    '''Retrieve a domain from given module.'''

    domain_cfg = module.build_domain()
    new_domain = default_domain()
    new_domain.update(**domain_cfg)
    return new_domain


def default_domain():
    '''Default PyEve domain parameters. This may be overrided.'''

    return {
        # 'title' tag used in item links. Defaults to the resource title minus
        # the final, plural 's' (works fine in most cases but not for 'people')
        # 'item_title': 'person',

        # by default the standard item entry point is defined as
        # '/people/<ObjectId>'. We leave it untouched, and we also enable an
        # additional read-only entry point. This way consumers can also perform
        # GET requests at '/people/<lastname>'.
        # 'additional_lookup': {
        #     'url': 'regex("[\w]+")',
        #     'field': 'lastname'
        # },

        # We choose to override global cache-control directives for this resource.
        'cache_control': 'max-age=10,must-revalidate',
        'cache_expires': 10,

        # most global settings can be overridden at resource level
        'resource_methods': ['GET', 'POST',],
    }