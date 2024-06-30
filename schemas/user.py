from pydantic import BaseModel, Field


class UserIn(BaseModel):
    name: str = Field(..., example="username")
    email: str = Field(..., example="user@gmail.com")
    password: str = Field(..., example="password")


class UserLogin(BaseModel):
    email: str = Field(..., example="user@gmail.com")
    password: str = Field(..., example="password")


class DbUser(BaseModel):
    name: str
    email: str
    role: str = Field(default="staff")
