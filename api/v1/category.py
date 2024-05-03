from fastapi import APIRouter, Header, status, HTTPException
from schemas.category import CategoryIn
from controller.category import CategoryController
from tools.keycloak import verify_token
from utils.checker import check_if_user_is_admin


category_router = APIRouter(prefix="/categories", tags=["category"])


@category_router.post("/",status_code=status.HTTP_200_OK)
def add_category(category: CategoryIn, token=Header(...)):
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid token")
    if not check_if_user_is_admin(payload):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="user is not admin")
    item = CategoryController.add_category(category)
    return item