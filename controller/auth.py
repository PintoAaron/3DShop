from fastapi import HTTPException, status
from schemas.user import UserIn, UserLogin, DbUser
from schemas.token import Token
from utils import sql
from tools.keycloak import login_keycloak_user, register_keycloak_user


class AuthContoller:

    @classmethod
    def login(cls, customer: UserLogin) -> Token:
        if sql.get_user_by_email(customer.email):
            token = login_keycloak_user(customer)
            if token:
                return Token(**token)
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid password")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="no account found")

    @classmethod
    def register(cls, customer: UserIn) -> Token:
        if sql.get_user_by_email(customer.email):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="email already exists")
        if register_keycloak_user(customer):
            if sql.save_user_to_db(DbUser(name=customer.name, email=customer.email)):
                token = cls.login(UserLogin(
                    email=customer.email, password=customer.password))
                return token
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="unable to register customer")

        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="unable to register customer")
