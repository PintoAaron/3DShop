import sqlalchemy as sq
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from uuid import uuid4

from core import setup as db_setup 


class Orders(db_setup.Base):
    __tablename__ = 'orders'
    
    order_id = Column(String, primary_key=True, default=str(uuid4()))
    total_price = Column(Float,nullable=False)
    date_created = Column(DateTime,nullable=False, default=sq.func.now())
    customer_id = Column(Integer, sq.ForeignKey('customers.id'))
    customer = relationship('Customers',back_populates='orders')
    order_items = relationship('OrderItem',back_populates='order')
    
    
    def __str__(self):
        return f'{self.customer.name} - {self.total_price}'