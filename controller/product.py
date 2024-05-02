from fastapi import HTTPException,status
from schemas.customer import CustomerIn, CustomerLogin, DbCustomer
from schemas.token import Token
from typing import Dict
from utils import sql



class ProductContoller:
    
    
    def get_all_products():
        




