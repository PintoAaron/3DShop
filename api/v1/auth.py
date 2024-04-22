from fastapi import APIRouter
from controller.auth import AuthContoller
from schemas.customer import CustomerIn, CustomerLogin

auth_router = APIRouter(prefix="/auth", tags=["auth"])



@auth_router.post("/login")
def login(data:CustomerLogin):
    msg = AuthContoller.login(data)
    return msg


@auth_router.post("/register")
def register(data:CustomerIn):
    msg = AuthContoller.register(data)
    return msg
    