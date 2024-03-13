from fastapi import HTTPException,status
from jose import jwt,JWTError
from datetime import datetime, timedelta
import requests 

from config import settings
from schemas import customer as schema



setting = settings.AppSettings()


    
def login_keycloak_user(email: str, password: str) -> dict:
    
    "login user and get the token"
    
    login_data = {
        'grant_type': 'password',
        'client_id': setting.KEYCLOAK_CLIENT,
        'client_secret': setting.KEYCLOAK_CLIENT_SECRET,
        'username': email,
        'password': password,
    }
    url = f"{setting.KEYCLOAK_URL}/realms/{setting.KEYCLOAK_REALM}/protocol/openid-connect/token"
    try:
        response = requests.post(url, data=login_data)
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid credentials")
    


"login admin user and get the token to be used for user registration"

admin_token = login_keycloak_user(setting.KEYCLOAK_ADMIN, setting.KEYCLOAK_ADMIN_PASSWORD)
print(f"admin token: {admin_token}")
access_token_expire_date = datetime.now() + timedelta(seconds=admin_token.get('expires_in'))
print(f"token expires in: {access_token_expire_date}")
refresh_token_expire_date = datetime.now() + timedelta(seconds=admin_token.get('refresh_expires_in'))




def refresh_user_token():
    
    "refresh user token and return the new token"
    
    keycloak_login_data = {
        'grant_type': 'refresh_token',
        'client_id': setting.KEYCLOAK_CLIENT,
        'client_secret': setting.KEYCLOAK_CLIENT_SECRET,
        'refresh_token': admin_token.get('refresh_token'),
    }
    url = f"{setting.KEYCLOAK_URL}/realms/{setting.KEYCLOAK_REALM}/protocol/openid-connect/token"
    try:
        response = requests.post(url, data=keycloak_login_data)
        return response.json()
    except Exception as e:  
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid credentials")





def refresh_or_get_new_admin_token():
    
    "refresh admin token if expired else return the token"
    
    global admin_token, access_token_expire_date,refresh_token_expire_date
    if datetime.now() > access_token_expire_date:
        if datetime.now() > refresh_token_expire_date:
            admin_token = login_keycloak_user(setting.KEYCLOAK_ADMIN)
            access_token_expire_date = datetime.now() + timedelta(seconds=admin_token.get('expires_in'))
            refresh_token_expire_date = datetime.now() + timedelta(seconds=admin_token.get('refresh_expires_in'))
        else:
            admin_token = refresh_user_token()
            access_token_expire_date = datetime.now() + timedelta(seconds=admin_token.get('expires_in'))
            refresh_token_expire_date = datetime.now() + timedelta(seconds=admin_token.get('refresh_expires_in'))
    return admin_token



def register_keycloak_user( customer_details: schema.CustomerBase ):
    
    "register user in keycloak and return status code of the request"
    
    username = customer_details.first_name[0].lower() + customer_details.last_name.lower()
    register_data = {
        "username": username,
        "firstName": customer_details.first_name,
        "lastName": customer_details.last_name,
        "email": customer_details.email,
        "enabled": True,
        "credentials": [
            {
                "type": "password",
                "value": customer_details.password,
                "temporary": False
            }
        ],
    }
    admin_token = refresh_or_get_new_admin_token()
    headers = {
        "Authorization": f"Bearer {admin_token.get('access_token')}",
        "Content-Type": "application/json"
    }
    url = f"{setting.KEYCLOAK_URL}/admin/realms/{setting.KEYCLOAK_REALM}/users"
    try:
        response = requests.post(url, json=register_data, headers=headers)
        return True if response.status_code == 201 else False
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid credentials")
    



DECODE_KEY= "-----BEGIN PUBLIC KEY-----\n" + setting.PUBLIC_KEY + "\n-----END PUBLIC KEY-----"


def verify_token(token: str):
    
    "verify token and return payload if valid else raise exception"
    
    try:
        payload = jwt.decode(token, key=DECODE_KEY, audience=setting.AUDIENCE, algorithms=[setting.ALGORITHM])
        return payload
    except JWTError as e:
        raise HTTPException(status_code=401, detail=str(e))

