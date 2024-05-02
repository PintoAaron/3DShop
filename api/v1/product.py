from fastapi import APIRouter,Header,status ,HTTPException
from tools.keycloak import verify_token
from utils.checker import check_if_user_is_admin




product_router = APIRouter(prefix="/products", tags=["product"])



@product_router.post("/",status_code=status.HTTP_200_OK)
def get_products(token=Header(...)):
    print(token)
    payload = verify_token(token)
    print(payload)
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="invalid token")
    if not check_if_user_is_admin(payload):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="admins only")
    