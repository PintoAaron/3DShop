from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import ForeignKey, func
from datetime import datetime

from core.setup import Base


class ProductImageModel(Base):
    __tablename__ = "product_image"

    id: Mapped[int] = mapped_column(primary_key=True)
    image_url: Mapped[str]
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id", ondelete="CASCADE"))
    created_at: Mapped[datetime] = mapped_column(insert_default=func.now())

    product: Mapped["ProductModel"] = relationship(back_populates="images", passive_deletes="all")
