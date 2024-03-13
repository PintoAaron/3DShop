from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import settings

setting = settings.AppSettings()


class DatabaseSetup:
    def __init__(self):
        self.engine = create_engine(setting.DATABASE_URL)
        self.session_maker = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.Base = declarative_base()
    
    def get_session(self) -> sessionmaker:
        return self.session_maker
    
    def get_base(self):
        return self.Base
    
    def get_engine(self):
        return self.engine
    
  
database = DatabaseSetup()
Base = database.get_base()