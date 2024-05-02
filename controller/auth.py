from fastapi import HTTPException,status
from schemas.customer import CustomerIn, CustomerLogin, DbCustomer
from schemas.token import Token
from typing import Dict
from utils import sql
from tools.keycloak import login_keycloak_user,register_keycloak_user


class AuthContoller:
    
    @classmethod
    def login(cls,customer: CustomerLogin) -> Token:
        if sql.get_customer_by_email(customer.email):
            token = login_keycloak_user(customer)
            if token:
                return Token(**token)
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="invalid password")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="no account found")
        
        

    @classmethod
    def register(cls,customer: CustomerIn) -> Token:
        if sql.get_customer_by_email(customer.email):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="email already exists")
        if register_keycloak_user(customer):
            if sql.save_customer_to_db(DbCustomer(name=customer.name,email=customer.email)):
                token = cls.login(CustomerLogin(email=customer.email,password=customer.password))
                return token
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="unable to register customer")
        
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="unable to register customer")
    