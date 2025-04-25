from typing import Annotated
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.schema import ForeignKey
from database import Base
from datetime import datetime

my_id = Annotated[int, mapped_column(primary_key=True)]

class Post(Base):
    __tablename__ = "post"

    id: Mapped[my_id]
    name: Mapped[str]

class Teacher(Base):
    __tablename__ = "teacher"

    person_id: Mapped[int] = mapped_column(ForeignKey("person.id", ondelete="CASCADE"), primary_key=True)
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id", ondelete="CASCADE"), primary_key=True)


class Item(Base):
    __tablename__ = "item"

    id: Mapped[my_id]
    name: Mapped[str]
    post: Mapped[int] = mapped_column(ForeignKey("post.id", ondelete="CASCADE"))


class Group(Base):
    __tablename__ = "group"

    id: Mapped[my_id]
    name: Mapped[str]
    professions: Mapped[bool] = mapped_column(default=False)
    denominator: Mapped[bool] = mapped_column(default=False)


class Grade(Base):
    __tablename__ = "grade"

    id: Mapped[my_id]
    teacher: Mapped[int] = mapped_column(ForeignKey("person.id", ondelete="CASCADE"))
    student: Mapped[int] = mapped_column(ForeignKey("person.id", ondelete="CASCADE"))
    evaluation: Mapped[int]
    truancy: Mapped[bool]
    date: Mapped[datetime]
    number_couple: Mapped[int]
