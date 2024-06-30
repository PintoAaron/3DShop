from fastapi import APIRouter,Header,status ,HTTPException
from tools.keycloak import verify_token
from utils.checker import check_if_user_is_admin
from schemas.product import ProductModel
from controller.product import ProductContoller


product_router = APIRouter(prefix="/products", tags=["PRODUCT"])

@product_router.post("/", status_code=status.HTTP_200_OK)
def add_product(item: ProductModel, token=Header(...)):
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid token")
    if not check_if_user_is_admin(payload):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="user is not admin")
    product = ProductContoller.add_product(item)
    return product
    