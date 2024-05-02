from typing import Dict

def check_if_user_is_admin(data: Dict) -> bool:
    """
    Check if user is admin
    """
    resource_access = data.get("resource_access")
    if resource_access:
        realm_management = resource_access.get("realm_management")
        if realm_management:
            roles = realm_management.get("roles")
            if roles:
                if "realm-admin" in roles:
                    return True
    return False