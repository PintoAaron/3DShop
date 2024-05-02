from fastapi import APIRouter
from controller.auth import AuthContoller
from schemas.customer import CustomerIn, CustomerLogin
from schemas.token import Token

auth_router = APIRouter(prefix="/auth", tags=["auth"])



@auth_router.post("/login")
def login(data:CustomerLogin) -> Token:
    msg = AuthContoller.login(data)
    return msg


@auth_router.post("/register")
def register(data:CustomerIn) -> Token:
    msg = AuthContoller.register(data)
    return msg

    