from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID 
from uuid import uuid4
from typing import List

from core.setup import Base


class CartModel(Base):
    __tablename__ = 'cart'
    
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    cart_items: Mapped[List["CartItemModel"]] = relationship(back_populates="cart",
                                                             passive_deletes="all")
