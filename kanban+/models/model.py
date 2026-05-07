from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)
from ..db.base import Base
from typing import List

class User(Base):
    __tablename__ = 'users'
    id : Mapped[int] = mapped_column(init=False, primary_key=True)
    avatar_url: Mapped[str | None] = mapped_column(nullable=False, default=None)
    name : Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    senha: Mapped[str] = mapped_column(nullable=False)
    admin: Mapped[bool] = mapped_column(default=False)
    active: Mapped[bool] = mapped_column(default=True)

    tasks_assigend: Mapped[List["Task"]] = relationship(back_populates="assingee", default_factory=List)

