from schemas.customer import CustomerIn, CustomerLogin
from typing import Dict
from utils import sql,generate


class AuthContoller:
    
    @classmethod
    def login(cls,customer: CustomerLogin) -> Dict:
        user = sql.get_customer_by_email(customer.email)
        if user:
            if generate.verify_password(customer.password,user.password):
                return {"token":"token"}
            return {"message":"invalid password"}
        return {"message":"no account found with that email address"}
        
        

    @classmethod
    def register(cls,customer: CustomerIn) -> Dict:
        if sql.get_customer_by_email(customer.email):
            return {"message":"customer already exists"}
        password = customer.password
        customer.password = generate.hash_password(customer.password)
        is_registerd = sql.save_customer_to_db(customer)
        if is_registerd:
            token = cls.login(CustomerLogin(email=customer.email,password=password))
            return token
        return {"message":"unable to register customer"}
            
    