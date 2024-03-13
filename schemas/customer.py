from pydantic import BaseModel, EmailStr


class CustomerBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    phone: str
    

class CustomerIn(BaseModel):
    email: EmailStr
    password: str
    

class CustomerOut(BaseModel):
    email: EmailStr