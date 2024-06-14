from fastapi import APIRouter, Header, status, HTTPException
from schemas.category import CategoryIn, CategoryOut
from controller.category import CategoryController
from tools.keycloak import verify_token
from utils.checker import check_if_user_is_admin
from typing import List


category_router = APIRouter(prefix="/categories", tags=["category"])


@category_router.post("/",status_code=status.HTTP_200_OK)
def add_category(category: CategoryIn, token=Header(...)):
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid token")
    if not check_if_user_is_admin(payload):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="permission denied")
    item = CategoryController.add_category(category)
    return item


@category_router.get("/",status_code=status.HTTP_200_OK, response_model=List[CategoryOut])
def get_all_categories():
    """
    Get all categories
    """
    result = CategoryController.get_all_categories()
    return result


@category_router.get("/{cat_id}",status_code=status.HTTP_200_OK, response_model=CategoryOut)
def get_category(cat_id: int):
    """
    Get a category by id
    """
    item = CategoryController.get_category_by_id(cat_id)
    if item:
        return item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="category not found")



@category_router.put("/{cat_id}",status_code=status.HTTP_200_OK, response_model=CategoryOut)
def update_category(cat_id: int, category: CategoryIn, token=Header(...)):
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid token")
    if not check_if_user_is_admin(payload):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="permission denied")
    item = CategoryController.update_category(cat_id, category)
    if item:
        return item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="category not found")



@category_router.delete("/{cat_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_category(cat_id: int, token=Header(...)):
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid token")
    if not check_if_user_is_admin(payload):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="permission denied")
    item = CategoryController.delete_category(cat_id)
    if item:
        return item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="category not found")