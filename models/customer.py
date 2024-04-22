import sqlalchemy as sq
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


from core import setup as db_setup 


class Customers(db_setup.Base):
    __tablename__ = 'customers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String,nullable=False)
    email = Column(String,nullable=False)
    phone = Column(String,nullable=True)
    password = Column(String,nullable=False)
    orders = relationship('Orders',back_populates='customer')
    
    def __str__(self):
        return self.name
    
    