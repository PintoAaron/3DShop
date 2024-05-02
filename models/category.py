from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


from core import setup as db_setup 


class Category(db_setup.Base):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True)
    name = Column(String,nullable=False)
    description = Column(String,nullable=False)
    products = relationship('Products',back_populates='category')
    
    
    def __str__(self):
        return self.name
    