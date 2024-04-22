from pydantic import BaseModel



class CustomerIn(BaseModel):
    name: str
    email: str
    phone: str = None
    password: str
    
    
    
class CustomerLogin(BaseModel):
    email: str
    password: str


class CustomerOut(BaseModel):
    token : str