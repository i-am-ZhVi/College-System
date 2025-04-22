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
    patronymic: Mapped[str]
    role: Mapped[Role]


class Post(Base):
    __tablename__ = "post"

    id: Mapped[my_id]
    name: Mapped[str]


class Teacher(Base):
    __tablename__ = "teacher"

    id: Mapped[my_id]
    person_id: Mapped[int] = mapped_column(ForeignKey("person.id", ondelete="CASCADE"))
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id", ondelete="CASCADE"))
