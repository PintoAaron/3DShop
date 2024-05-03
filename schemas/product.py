from pydantic import BaseModel




class ProductModel(BaseModel):
    name : str
    price : float
    category: int
    quantity : int