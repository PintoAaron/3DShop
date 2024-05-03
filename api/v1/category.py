from fastapi import APIRouter, Header, status
from schemas.category import CategoryIn
from controller.category import CategoryController


category_router = APIRouter(prefix="/categories", tags=["category"])


@category_router.post("/",status_code=status.HTTP_200_OK)
def add_category(category: CategoryIn):
    item = CategoryController.add_category(category)
    return item