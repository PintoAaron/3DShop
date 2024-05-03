from fastapi import HTTPException,status
from schemas.product import ProductModel
from utils import sql



class CategoryController():
    
    def add_category(category):
        """
        Add a category
        """
        new_category = sql.save_category_to_db(category)
        if new_category:
            return new_category
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="unable to add category")
        
