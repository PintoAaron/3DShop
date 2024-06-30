from fastapi import APIRouter
from controller.auth import AuthContoller
from schemas.user import UserIn, UserLogin
from schemas.token import Token

auth_router = APIRouter(prefix="/auth", tags=["AUTHENTICATION"])


@auth_router.post("/login", response_model=Token)
def login_user(data:UserLogin):
    result = AuthContoller.login(data)
    return result


@auth_router.post("/register",response_model=Token)
def register_user(data:UserIn):
    result = AuthContoller.register(data)
    return result
