from fastapi import APIRouter, Header
from controller.auth import AuthContoller
from schemas.customer import CustomerIn, CustomerLogin
from schemas.token import Token

auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.post("/login", response_model=Token)
def login(data:CustomerLogin):
    result = AuthContoller.login(data)
    return result


@auth_router.post("/register",response_model=Token)
def register(data:CustomerIn):
    result = AuthContoller.register(data)
    return result
