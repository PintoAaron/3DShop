import sqlalchemy as sq
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ENUM
import enum


from core import setup as db_setup 



class RoleType(enum.Enum):
    staff= "staff"
    admin= "admin"


class Customers(db_setup.Base):
    __tablename__ = 'customers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String,nullable=False)
    email = Column(String,nullable=False)
    role = Column(ENUM(RoleType,name='role'),default='staff')
    orders = relationship('Orders',back_populates='customer')
    
    def __str__(self):
        return self.name
    
    