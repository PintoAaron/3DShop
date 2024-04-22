from sqlalchemy.orm import Session
from core import setup


class DBSession:
    def __init__(self):
        self.db_init= setup.db
        self.db = self.db_init.get_session()
        
    def __enter__(self) -> Session:
        return self.db
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.db.close()