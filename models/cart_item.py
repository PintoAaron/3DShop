from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import ForeignKey

from core.setup import Base


class CartItemModel(Base):
    __tablename__ = 'cart_item'

    id: Mapped[int] = mapped_column(primary_key=True)
    cart_id: Mapped[UUID] = mapped_column(ForeignKey("cart.id", ondelete="CASCADE"))
    product: Mapped[int] = mapped_column(ForeignKey("product.id", ondelete="CASCADE"))
    quantity: Mapped[int]

    cart: Mapped["CartModel"] = relationship(back_populates="cart_items",
                                             passive_deletes="all")
