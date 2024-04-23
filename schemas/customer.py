from pydantic import BaseModel



class CustomerIn(BaseModel):
    name: str
    email: str
    password: str
    
    
    
class CustomerLogin(BaseModel):
    email: str
    password: str


class CustomerOut(BaseModel):
    token : str