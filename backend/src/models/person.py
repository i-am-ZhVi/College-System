import enum

from typing import Annotated
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.schema import ForeignKey
from database import Base


my_id = Annotated[int, mapped_column(primary_key=True)]


class Role(enum.Enum):
    head = "head"
    teacher = "teacher"
    student = "student"


class Person(Base):
    __tablename__ = "person"

    id: Mapped[my_id]
    surname: Mapped[str]
    name: Mapped[str]
    patronymic: Mapped[str] = mapped_column(nullable=True)
    phone: Mapped[str] = mapped_column(nullable=True)
    role: Mapped[Role] = mapped_column(default=Role.student, server_default="student")


class Login(Base):
    __tablename__ = "login"

    person_id: Mapped[int] = mapped_column(ForeignKey("person.id", ondelete="CASCADE"), primary_key=True)
    login: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
