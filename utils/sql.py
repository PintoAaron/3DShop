from typing import Any
from utils import session
from models import database_models as db




def add_object_to_database(item: Any) -> bool:
    
    """add object to database"""
    
    with session.CreateDBSession() as db_session:
        db_session.add(item)
        db_session.commit()
        db_session.refresh(item)
        return True
    


def add_customer_to_database(customer_details: dict) -> bool:
    """add customer to database"""
    try:
        with session.CreateDBSession() as db_session:
            new_customer = db.Customer(**customer_details.dict())
            add_object_to_database(new_customer)
            db_session.commit()
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    

def check_if_customer_exists(email: str) -> bool:
    
    """check if customer exists in database"""
    
    with session.CreateDBSession() as db_session:
        return db_session.query(db.Customer).filter(db.Customer.email == email).first() is not None