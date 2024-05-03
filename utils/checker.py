from typing import Dict

def check_if_user_is_admin(data) -> bool:
    """
    Check if user is admin
    """
    resource_access = data["resource_access"]
    if resource_access:
        try:
            realm_management = resource_access["realm-management"]
        except KeyError:
            return False
        if realm_management:
            roles = realm_management["roles"]
            if roles:
                if "realm-admin" in roles:
                    return True
    return False