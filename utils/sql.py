from utils.session import DBSession
from models.customer import Customers
from models.product import Products
from models.category import Category
from sqlalchemy.exc import SQLAlchemyError
from schemas import customer,product,category
from tools.log import Log
from typing import Union
from config import setting


settings = setting.AppSettings()


logger = Log(__name__)


def add_admin_user_to_db():
    try:
        with DBSession() as db:
            admin = db.query(Customers).filter(Customers.email == settings.KEYCLOAK_ADMIN_EMAIL).first()
            if admin:
                return "success - admin user already exists"
            admin = Customers(name=settings.KEYCLOAK_ADMIN_USER, email=settings.KEYCLOAK_ADMIN_EMAIL)
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
        

def save_customer_to_db(customer: customer.DbCustomer) -> Union[bool,Customers]:
    user = Customers(**customer.dict())
    try:
        return add_object_to_database(user)
    except SQLAlchemyError as e:
        logger.error(f"Error saving customer to database --- {e}")
        return False


def get_customer_by_email(email: str):
    try:
        with DBSession() as db:
            return db.query(Customers).filter(Customers.email == email).first()
    except SQLAlchemyError as e:
        logger.error(f"Error getting customer by email --- {e}")
        return None


def save_product_to_db(product: product.ProductModel):  
    with DBSession() as db:
        category = db.query(Category).filter(Category.id == product.category).first()
        if not category:
            return False
    new_product = Products(category=category, **product.dict(exclude={"category"}))
    try:
        return add_object_to_database(new_product)
    except SQLAlchemyError as e:
        logger.error(f"Error saving product to database --- {e}")
        return False       



def get_product_by_name(name: str):
    try:
        with DBSession() as db:
            return db.query(Products).filter(Products.name == name).first()
    except SQLAlchemyError as e:
        logger.error(f"Error getting product by name --- {e}")
        return None
    

def update_product_quantity(name: str,quantity: int):
    try:
        with DBSession() as db:
            product = db.query(Products).filter(Products.name == name).first()
            product.quantity = quantity
            db.commit()
            db.refresh(product)
            return product
    except SQLAlchemyError as e:
        logger.error(f"Error updating product quantity --- {e}")
        return False


def save_category_to_db(category: category.CategoryIn) -> Union[bool,Category]:
    new_category = Category(**category.dict())
    try:
        return add_object_to_database(new_category)
    except SQLAlchemyError as e:
        logger.error(f"Error saving category to database --- {e}")
        return False
    
    
def get_all_categories():
    try:
        with DBSession() as db:
            return db.query(Category).all()
    except SQLAlchemyError as e:
        logger.error(f"Error getting all categories --- {e}")
        return None
    


def get_category_by_id(cat_id: int):
    try:
        with DBSession() as db:
            return db.query(Category).filter(Category.id == cat_id).first()
    except SQLAlchemyError as e:
        logger.error(f"Error getting category by id --- {e}")
        return None 
    


def update_category(cat_id: int, item: category.CategoryIn):
    try:
        with DBSession() as db:
            category = db.query(Category).filter(Category.id == cat_id).first()
            if not category:
                return False
            category.name = item.name
            category.description = item.description
            db.commit()
            db.refresh(category)
            return category  
    except SQLAlchemyError as e:
        logger.error(f"Error updating category --- {e}")
        return False
    
    

def get_products_by_category(cat_id: int):
    try:
        with DBSession() as db:
            return db.query(Products).filter(Products.category_id == cat_id).all()
    except SQLAlchemyError as e:
        logger.error(f"Error getting products by category --- {e}")
        return None
    
    
def delete_category(cat_id: int):
    try:
        with DBSession() as db:
            category = db.query(Category).filter(Category.id == cat_id).first()
            if not category:
                return False
            db.delete(category)
            db.commit()
            return True
    except SQLAlchemyError as e:
        logger.error(f"Error deleting category --- {e}")
        return False



