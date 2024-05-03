from sqlalchemy import Column, Integer, String, Float,ForeignKey
from sqlalchemy.orm import relationship

from core import setup as db_setup


class Products(db_setup.Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String,nullable=False)
    price = Column(Float,nullable=False)
    quantity = Column(Integer,nullable=False)
    order_items = relationship('OrderItem',back_populates='product')
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category',back_populates='products')
     
    
    def __str__(self):
        return self.name