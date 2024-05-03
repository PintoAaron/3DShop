from typing import Dict

def check_if_user_is_admin(data) -> bool:
    """
    Check if user is admin
    """
    print("data",data)
    resource_access = data.get("resource_access")
    print(resource_access)
    if resource_access:
        realm_management = resource_access.get("realm_management")
        print(realm_management)
        if realm_management:
            roles = realm_management.get("roles")
            print(roles)
            if roles:
                if "realm-admin" in roles:
                    return True
    return False