from fastapi import HTTPException,status
from schemas.customer import CustomerIn, CustomerLogin
from typing import Dict
from utils import sql
from tools.keycloak import login_keycloak_user,register_keycloak_user


class AuthContoller:
    
    @classmethod
    def login(cls,customer: CustomerLogin):
        user = sql.get_customer_by_email(customer.email)
        if user:
            token = login_keycloak_user(customer)
            if token:
                return token
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="invalid email or password")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="no account found with email")
        
        

    @classmethod
    def register(cls,customer: CustomerIn):
        if sql.get_customer_by_email(customer.email):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="email already exists")
        user = register_keycloak_user(customer)
        print(user)
        if user:
            is_registerd = sql.save_customer_to_db(customer)
            if is_registerd:
                token = cls.login(CustomerLogin(email=customer.email,password=customer.password))
                return token
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="unable to register customer")
        
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="unable to register customer")
            
    