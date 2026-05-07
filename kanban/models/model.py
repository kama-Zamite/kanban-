from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)
from sqlalchemy import ForeignKey
from ..db.base import Base
from typing import List

class User(Base):
    __tablename__ = 'users'
    id : Mapped[int] = mapped_column(init=False, primary_key=True)
    name : Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    senha: Mapped[str] = mapped_column(nullable=False)
    admin: Mapped[bool] = mapped_column(default=False)
    active: Mapped[bool] = mapped_column(default=True)
    avatar_url: Mapped[str | None] = mapped_column(nullable=False, default=None)

    tasks_assigend: Mapped[List["Task"]] = relationship(back_populates="assingee", default_factory=List)


class Task(Base):
    __tablename__ = 'tasks'
    id : Mapped[int] = mapped_column(init=False, primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str | None] = mapped_column(nullable=True, default=None)
    priority: Mapped[str] = mapped_column(default='Baixa')
    creater_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    creater: Mapped['User'] = relationship(init=False)

    # assingee: 