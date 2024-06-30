from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import ForeignKey, func
from datetime import datetime
from typing import List

from core.setup import Base


class ProductModel(Base):
    __tablename__ = 'product'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    price: Mapped[float]
    quantity: Mapped[int]
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id", ondelete="RESTRICT"))
    date_created: Mapped[datetime] = mapped_column(insert_default=func.now())

    order_items: Mapped["OrderItemModel"] = relationship(back_populates="product", 
                                                         passive_deletes="all")
    category: Mapped["CategoryModel"] = relationship(back_populates="products", 
                                                     passive_deletes="all")
    images: Mapped[List["ProductImageModel"]] = relationship(back_populates="product", 
                                                             passive_deletes="all")
