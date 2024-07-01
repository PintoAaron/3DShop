from fastapi import HTTPException, status
from schemas.product import ProductModel
from utils import sql


class ProductContoller:

    def add_product(item: ProductModel):
        """
        Add a product
        """
        old_product = sql.get_product_by_name(item.name)
        if old_product:
            product = sql.update_product_quantity(
                item.name, old_product.quantity + item.quantity)
            if product:
                return product
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="unable to update product")
        new_product = sql.save_product_to_db(item)
        if new_product:
            return new_product
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="unable to add product")
