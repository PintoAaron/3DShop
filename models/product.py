import sqlalchemy as sq
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from core import setup as db_setup


class Products(db_setup.Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String,nullable=False)
    price = Column(Float,nullable=False)
    order_items = relationship('OrderItem',back_populates='product')
    
    def __str__(self):
        return self.name