from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import Optional, List

from core.setup import Base


class CategoryModel(Base):
    __tablename__ = 'category'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str]]

    products: Mapped[List["ProductModel"]] = relationship(back_populates="category",
                                                          passive_deletes="all")
