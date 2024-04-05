import sqlalchemy as sq
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from core import setup as db_setup



class OrderItem(db_setup.Base):
    __tablename__ = 'order_items'
    
    id = Column(Integer, primary_key=True)
    order_id = Column(String, sq.ForeignKey('orders.order_id'))
    product_id = Column(Integer, sq.ForeignKey('products.id'))
    quantity = Column(Integer,nullable=False)
    price = Column(Float,nullable=False)
    order = relationship('Orders',back_populates='order_items')
    product = relationship('Products',back_populates='order_items')
    
    def __str__(self):
        return f'{self.product.name} - {self.quantity} - {self.price}' 