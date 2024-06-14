from pydantic import BaseModel



class CategoryIn(BaseModel):
    name: str
    description: str
    
    
class CategoryOut(BaseModel):
    id: int
    name: str
    description: str