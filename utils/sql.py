from utils.session import DBSession
from models.user import UserModel
from models.product import ProductModel
from models.category import CategoryModel
from sqlalchemy.exc import SQLAlchemyError
from schemas import product, category, user
from tools.log import Log
from typing import Union
from config import setting


settings = setting.AppSettings()


logger = Log(__name__)


def add_admin_user_to_db():
    try:
        with DBSession() as db:
            admin = db.query(UserModel).filter(UserModel.email ==
                                               settings.KEYCLOAK_ADMIN_EMAIL).first()
            if admin:
                return "success - admin user already exists"
            admin = UserModel(name=settings.KEYCLOAK_ADMIN_USER,
                              email=settings.KEYCLOAK_ADMIN_EMAIL)
            db.add(admin)
            db.commit()
            return "success - admin user added"
    except SQLAlchemyError as e:
        logger.error(f"Error adding admin user to database --- {e}")
        return "error - admin user not added"


def add_object_to_database(item: any):
    with DBSession() as db:
        try:
            db.add(item)
            db.commit()
            db.refresh(item)
            return item
        except SQLAlchemyError:
            db.rollback()


def save_user_to_db(user_schema: user.DbUser) -> Union[bool, UserModel]:
    user_object = UserModel(**user_schema.dict())
    try:
        return add_object_to_database(user_object)
    except SQLAlchemyError as e:
        logger.error(f"Error saving customer to database --- {e}")
        return False


def get_user_by_email(email: str):
    try:
        with DBSession() as db:
            return db.query(UserModel).filter(UserModel.email == email).first()
    except SQLAlchemyError as e:
        logger.error(f"Error getting customer by email --- {e}")
        return None


def save_product_to_db(product_schema: product.ProductModel):
    with DBSession() as db:
        category = db.query(CategoryModel).filter(
            CategoryModel.id == product_schema.category).first()
        if not category:
            return False
    product_object = ProductModel(
        category=category, **product_schema.dict(exclude={"category"}))
    try:
        return add_object_to_database(product_object)
    except SQLAlchemyError as e:
        logger.error(f"Error saving product to database --- {e}")
        return False


def get_product_by_name(name: str):
    try:
        with DBSession() as db:
            return db.query(ProductModel).filter(ProductModel.name == name).first()
    except SQLAlchemyError as e:
        logger.error(f"Error getting product by name --- {e}")
        return None


def update_product_quantity(name: str, quantity: int):
    try:
        with DBSession() as db:
            product = db.query(ProductModel).filter(ProductModel.name == name).first()
            product.quantity = quantity
            db.commit()
            db.refresh(product)
            return product
    except SQLAlchemyError as e:
        logger.error(f"Error updating product quantity --- {e}")
        return False


def save_category_to_db(category_schema: category.CategoryIn) -> Union[bool, CategoryModel]:
    category_object = CategoryModel(**category_schema.dict())
    try:
        return add_object_to_database(category_object)
    except SQLAlchemyError as e:
        logger.error(f"Error saving category to database --- {e}")
        return False


def get_all_categories():
    try:
        with DBSession() as db:
            return db.query(CategoryModel).all()
    except SQLAlchemyError as e:
        logger.error(f"Error getting all categories --- {e}")
        return None


def get_category_by_id(cat_id: int):
    try:
        with DBSession() as db:
            return db.query(CategoryModel).filter(CategoryModel.id == cat_id).first()
    except SQLAlchemyError as e:
        logger.error(f"Error getting category by id --- {e}")
        return None


def update_category(cat_id: int, item: category.CategoryIn):
    try:
        with DBSession() as db:
            category_object = db.query(CategoryModel).filter(
                CategoryModel.id == cat_id).first()
            if not category_object:
                return False
            category_object.name = item.name
            category_object.description = item.description
            db.commit()
            db.refresh(category_object)
            return category_object
    except SQLAlchemyError as e:
        logger.error(f"Error updating category --- {e}")
        return False


def get_products_by_category(cat_id: int):
    try:
        with DBSession() as db:
            return db.query(ProductModel).filter(ProductModel.category_id == cat_id).all()
    except SQLAlchemyError as e:
        logger.error(f"Error getting products by category --- {e}")
        return None


def delete_category(cat_id: int):
    try:
        with DBSession() as db:
            category_object = db.query(CategoryModel).filter(
                CategoryModel.id == cat_id).first()
            if not category_object:
                return False
            db.delete(category_object)
            db.commit()
            return True
    except SQLAlchemyError as e:
        logger.error(f"Error deleting category --- {e}")
        return False
