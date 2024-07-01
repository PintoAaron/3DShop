from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import func, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from typing import List
from uuid import uuid4

from core.setup import Base


class OrderModel(Base):
    __tablename__ = 'orders'

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid4)
    total_price: Mapped[float]
    order_date: Mapped[datetime] = mapped_column(insert_default=func.now())
    customer_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="RESTRICT"))

    user: Mapped["UserModel"] = relationship(back_populates='orders',
                                             passive_deletes="all")
    order_items: Mapped[List["OrderItemModel"]] = relationship(back_populates="order",
                                                               passive_deletes="all")
