from utils.session import DBSession
from models.customer import Customers
from sqlalchemy.exc import SQLAlchemyError
from schemas.customer import CustomerIn, DbCustomer
from tools.log import Log


logger = Log(__name__)


def add_object_to_database(item: any) -> bool:
    with DBSession() as db:
        try:
            db.add(item)
            db.commit()
            db.refresh(item)
            return True
        except SQLAlchemyError:
            db.rollback()
        

def save_customer_to_db(customer: DbCustomer) -> bool:
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