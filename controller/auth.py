from fastapi import HTTPException, status
from utils import sql, auth_services
from schemas.customer import CustomerBase,CustomerIn



class AuthCollection:
    
    
    def login(data: CustomerIn) -> dict:
        
        "login user and return the token"
        
        if not sql.check_if_customer_exists(data.email):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="No Account found with this email address")
        
        return auth_services.login_keycloak_user(data.email, data.password)
    
    
    
    def register_new_customer(data: CustomerBase) -> bool:
        
        "register user in keycloak and add user deatils to database"
        
        if sql.check_if_customer_exists(data.email):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="User already exists")#
        
        auth_services.register_keycloak_user(data)
        
        sql.add_customer_to_database(data)
        
        return True
        
        
            
    
    
    