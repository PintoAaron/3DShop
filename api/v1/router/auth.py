from typing import List, Dict
from fastapi import APIRouter
from controller.auth import AuthCollection
from schemas.customer import CustomerBase,CustomerIn,CustomerOut




auth_router = APIRouter(prefix="/auth")


@auth_router.post("/register",status_code=201,response_model=Dict[str, str])
def register(data: CustomerBase):
    AuthCollection.register_new_customer(data=data)
    return {"message":"account successfully registered","data":data.email}


@auth_router.post("/login")
def login(data: CustomerIn):
    response = AuthCollection.login(data=data)
    return response