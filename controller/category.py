from fastapi import HTTPException, status
from schemas.category import CategoryIn
from utils import sql


class CategoryController():

    def add_category(category: CategoryIn):
        """
        Add a category
        """
        new_category = sql.save_category_to_db(category)
        if new_category:
            return new_category
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="unable to add category")

    def get_all_categories():
        """
        Get all categories
        """
        return sql.get_all_categories()

    def get_category_by_id(cat_id: int):
        """
        Get a category by id
        """
        return sql.get_category_by_id(cat_id)

    def update_category(cat_id: int, category: CategoryIn):
        """
        Update a category
        """
        updated_category = sql.update_category(cat_id, category)
        if updated_category:
            return updated_category
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="unable to update category")

    def delete_category(cat_id: int):
        """
        Delete a category
        """

        deleted_category = sql.delete_category(cat_id)
        if deleted_category:
            return deleted_category
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="unable to delete category")
