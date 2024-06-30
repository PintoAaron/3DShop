from typing import Dict

def check_if_user_is_admin(data) -> bool:
    """
    Check if user is admin
    
    """
    print(data)
    if 'realm_access' in data and 'roles' in data['realm_access']:
        return True if "super_admin" in data['realm_access']['roles'] else False
    return False