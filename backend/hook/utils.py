from eve_auth_jwt import (
    get_request_auth_value,
    get_authen_roles,
)


def handle_resources_auth_user(on_resident, 
                               on_manager, 
                               resident_resources,
                               manager_resources,):
    def event_handler(resource, *args, **kwargs):
        args = (get_request_auth_value(), *args)
        if 'resident' in get_authen_roles() and resource in resident_resources:
            on_resident(*args, **kwargs)
        elif resource in manager_resources:
            on_manager(*args, **kwargs)
    return event_handler