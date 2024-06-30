from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy import func, Enum
from datetime import datetime
from typing import List
import enum

from core.setup import Base


class RoleType(enum.Enum):
    staff = "staff"
    admin = "admin"


class UserModel(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    role: Mapped[RoleType] = mapped_column(Enum(RoleType), default=RoleType.staff)
    date_joined: Mapped[datetime] = mapped_column(insert_default=func.now())

    orders: Mapped[List["OrderModel"]] = relationship(back_populates='user', 
                                                      passive_deletes="all")
