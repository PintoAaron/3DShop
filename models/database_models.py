import sqlalchemy as sq 
from sqlalchemy.orm import relationship
from core import setup
import uuid


class CartItem(setup.Base):
    __tablename__ = 'cart_item'
    
    id = sq.Column(sq.Integer, primary_key=True, index=True)
    cart_id = sq.Column(sq.String(100), sq.ForeignKey('cart.id'), index=True)
    product_id = sq.Column(sq.Integer, sq.ForeignKey('product.id'), index=True)
    quantity = sq.Column(sq.Integer, index=True)
    cart = relationship('Cart', back_populates='cart_items')
    product = relationship('Product', back_populates='cart_items')
    
    
    def __str__(self):
        return f"CartItem<{self.cart_id} - {self.product_id}>"
    
    


class Cart(setup.Base):
    __tablename__ = 'cart'
    
    id = sq.Column(sq.String(100), index=True,default=uuid.uuid4, primary_key=True)
    created_at = sq.Column(sq.DateTime, index=True, default=sq.sql.func.now())
    cart_items = relationship('CartItem',back_populates='cart')
    
    
    def __str__(self):
        return self.id
    
    

class Collection(setup.Base):
    __tablename__ = "collection"
    
    id = sq.Column(sq.Integer,primary_key=True,index=True)
    title = sq.Column(sq.String(50),index=True)
    featured = sq.Column(sq.String(200),index=True,nullable=True)
    products = relationship('Product',back_populates='collection')
    
    def __str__(self):
        return self.title
    
    

class Customer(setup.Base):
    __tablename__ = 'customer'
    
    id = sq.Column(sq.Integer, primary_key=True, index=True)
    first_name = sq.Column(sq.String(50), index=True)
    last_name = sq.Column(sq.String(50), index=True)
    email = sq.Column(sq.String(50), unique=True, index=True)
    password = sq.Column(sq.String(100))
    phone = sq.Column(sq.String(50), index=True)
    is_staff = sq.Column(sq.Boolean, default=False)
    orders = relationship('Order',back_populates='customer')
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    



class Order(setup.Base):
    __tablename__ = 'customer_order'
    
    id = sq.Column(sq.Integer, primary_key=True, index=True)
    customer_id = sq.Column(sq.Integer, sq.ForeignKey('customer.id'), index=True)
    product_id = sq.Column(sq.Integer, sq.ForeignKey('product.id'), index=True)
    quantity = sq.Column(sq.Integer, index=True)
    total = sq.Column(sq.Float, index=True)
    status = sq.Column(sq.String(50), index=True)
    date_created = sq.Column(sq.DateTime, default = sq.func.now())
    customer = relationship('Customer', back_populates='orders')
    product = relationship('Product', back_populates='order')
    
    
    def __str__(self):
        return f"Order<{self.customer_id} - {self.product_id}>"
    
  
  

class Product(setup.Base):
    __tablename__ = 'product'
    
    id = sq.Column(sq.Integer, primary_key=True, index=True)
    title = sq.Column(sq.String(50), index=True)
    description = sq.Column(sq.String(200), index=True)
    unit_price = sq.Column(sq.Float, index=True)
    inventory = sq.Column(sq.Integer, index=True)
    collection_id = sq.Column(sq.Integer, sq.ForeignKey('collection.id'), index=True)
    collection = relationship('Collection', back_populates='products')
    cart_items = relationship('CartItem',back_populates='product')
    order = relationship('Order',back_populates='product')
    
    def __str__(self):
        return self.title