from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import ForeignKey

from core.setup import Base


class OrderItemModel(Base):
    __tablename__ = 'order_item'

    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[UUID] = mapped_column(ForeignKey("orders.id", ondelete="RESTRICT"))
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id", ondelete="RESTRICT"))
    quantity: Mapped[int]
    price: Mapped[float]

    order: Mapped["OrderModel"] = relationship(back_populates="order_items", 
                                               passive_deletes="all")
    product: Mapped["ProductModel"] = relationship(back_populates="order_items", 
                                                   passive_deletes="all")
