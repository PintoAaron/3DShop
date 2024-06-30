from datetime import datetime, timedelta
from jose import JWTError, jwt
from config import setting
from schemas.customer import CustomerLogin, CustomerIn
from .log import Log
import requests


settings = setting.AppSettings()

logger = Log(__name__)

def login_keycloak_user(user: CustomerLogin):
    
    """
    login a user in keycloak
    
    """
    
    url = f"{settings.KEYCLOAK_URL}/realms/{settings.KEYCLOAK_REALM}/protocol/openid-connect/token"
    payload = {
        "client_id": settings.KEYCLOAK_CLIENT_ID,
        "client_secret": settings.KEYCLOAK_CLIENT_SECRET,
        "username": user.email,
        "password": user.password,
        "grant_type": "password"
    }
    try:
        response = requests.post(url, data=payload)
        return response.json() if response.status_code == 200 else None
    except Exception as e:
        print(f"Error login_keycloak_user: {e}")        
        logger.error(f"Error login_keycloak_user: {e}")
        return None



def login_keycloak_admin():
    
    """
    login admin user and use admin to perform operations
    
    """
    
    url = f"{settings.KEYCLOAK_URL}/realms/{settings.KEYCLOAK_REALM}/protocol/openid-connect/token"
    payload = {
        "client_id": settings.KEYCLOAK_CLIENT_ID,
        "client_secret": settings.KEYCLOAK_CLIENT_SECRET,
        "username": settings.KEYCLOAK_ADMIN_USER,
        "password": settings.KEYCLOAK_ADMIN_PASSWORD,
        "grant_type": "password"
    }
    
    
    try:
        response = requests.post(url, data=payload)
        return response.json()
    except Exception as e:
        print(f"Error login_keycloak_admin: {e}")        
        logger.error(f"Error login_keycloak_admin: {e}")
        return None



admin_token = login_keycloak_admin()
print(admin_token)
access_token_expire_date = datetime.now() + timedelta(seconds=admin_token.get("expires_in", 0))
refresh_token_expire_date = datetime.now() + timedelta(seconds=admin_token.get("refresh_expires_in", 0))


def refresh_user_token():
    
    """
    Refresh the user token
    """
    url = f"{settings.KEYCLOAK_URL}/realms/{settings.KEYCLOAK_REALM}/protocol/openid-connect/token"
    payload = {
        "client_id": settings.KEYCLOAK_CLIENT_ID,
        "client_secret": settings.KEYCLOAK_CLIENT_SECRET,
        "refresh_token": admin_token.get('refresh_token'),
        "grant_type": "refresh_token"
    }
    try:
        response = requests.post(url, data=payload)
        return response.json()
    except Exception as e:
        print(f"Error refresh_user_token: {e}")        
        logger.error(f"Error refresh_user_token: {e}")
        return None
    
    

def refresh_or_get_new_admin_token():
    
    """
    Refresh the admin token if it has expired, otherwise return the current token
     
    """
    
    global admin_token, access_token_expire_date, refresh_token_expire_date
    
    if datetime.now() > access_token_expire_date:
        if datetime.now() > refresh_token_expire_date:
            admin_token = login_keycloak_admin()
            access_token_expire_date = datetime.now() + timedelta(seconds=admin_token.get("expires_in", 0))
            refresh_token_expire_date = datetime.now() + timedelta(seconds=admin_token.get("refresh_expires_in", 0))
        else:
            admin_token = refresh_user_token()
            access_token_expire_date = datetime.now() + timedelta(seconds=admin_token.get("expires_in", 0))
            refresh_token_expire_date = datetime.now() + timedelta(seconds=admin_token.get("refresh_expires_in", 0))
    return admin_token



def register_keycloak_user(user: CustomerIn):
    
    """
    Register a user in keycloak
    
    """
    
    admin_token = refresh_or_get_new_admin_token()
    url = f"{settings.KEYCLOAK_URL}/admin/realms/{settings.KEYCLOAK_REALM}/users"
    headers = {
        "Authorization": f"Bearer {admin_token.get('access_token')}",
        "Content-Type": "application/json"
    }
    
    
    payload = {
        "username": user.email,
        "email": user.email,
        "firstName": user.name,
        "lastName": user.name,
        "enabled": True,
        "credentials": [
            {
                "type": "password",
                "value": user.password,
                "temporary": False
            }
        ],
        "attributes": {
            "user_role": "staff",
        }
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        return True if response.status_code == 201 else None
    except Exception as e:
        print(f"Error register_keycloak_user: {e}")
        logger.error(f"Error register_keycloak_user: {e}")
        return None
    
    
    
DECODE_KEY= "-----BEGIN PUBLIC KEY-----\n" + settings.PUBLIC_KEY + "\n-----END PUBLIC KEY-----"



def verify_token(token: str):
    
    try:
        payload = jwt.decode(token,key=DECODE_KEY,audience=settings.AUDIENCE,algorithms=[settings.ALGORITHM])
        return payload
    except JWTError as e:
        print(f"Error verify_token: {e}")
        logger.error(f"Error verify_token: {e}")
        return None