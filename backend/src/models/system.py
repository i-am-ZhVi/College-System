import enum

from typing import Annotated
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import expression
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
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id", ondelete="CASCADE"))


class Grade(Base):
    __tablename__ = "grade"

    id: Mapped[my_id]
    teacher_id: Mapped[int] = mapped_column(ForeignKey("person.id", ondelete="CASCADE"))
    student_id: Mapped[int] = mapped_column(ForeignKey("person.id", ondelete="CASCADE"))
    item_id: Mapped[int] = mapped_column(ForeignKey("item.id", ondelete="CASCADE"))
    evaluation: Mapped[int]
    truancy: Mapped[bool]
    date: Mapped[datetime]
    number_couple: Mapped[int]



class Group(Base):
    __tablename__ = "group"

    id: Mapped[my_id]
    name: Mapped[str]
    professions: Mapped[bool] = mapped_column(default=False, server_default=expression.false())
    denominator: Mapped[bool] = mapped_column(default=False, server_default=expression.false())


class Student_to_Group(Base):
    __tablename__ = "student_to_group"

    person_id: Mapped[int] = mapped_column(ForeignKey("person.id", ondelete="CASCADE"), primary_key=True)
    group_id: Mapped[int] = mapped_column(ForeignKey("group.id", ondelete="CASCADE"), primary_key=True)
    is_elder: Mapped[bool] = mapped_column(default=False, server_default=expression.false())


class Teacher_to_Group(Base):
    __tablename__ = "teacher_to_group"

    person_id: Mapped[int] = mapped_column(ForeignKey("person.id", ondelete="CASCADE"), primary_key=True)
    group_id: Mapped[int] = mapped_column(ForeignKey("group.id", ondelete="CASCADE"), primary_key=True)
    is_master: Mapped[bool] = mapped_column(default=False, server_default=expression.false())


class Item_for_Group(Base):
    __tablename__ = "item_for_group"

    group_id: Mapped[int] = mapped_column(ForeignKey("group.id", ondelete="CASCADE"), primary_key=True)
    item_id: Mapped[int] = mapped_column(ForeignKey("item.id", ondelete='CASCADE'), primary_key=True)


class Days(enum.Enum):
    mondey = "Понедельник"



class Specialties(Base):
    __tablename__ = "specialties"

    id: Mapped[my_id]
    weekly_day: Mapped[Days]
    teacher_id: Mapped[int] = mapped_column(ForeignKey("person.id", ondelete="CASCADE"))
    group_id: Mapped[int] = mapped_column(ForeignKey("group.id", ondelete="CASCADE"))
    item_id: Mapped[int] = mapped_column(ForeignKey("item.id", ondelete="CASCADE"))
    number_couple: Mapped[int]
    distance: Mapped[bool] = mapped_column(default=False, server_default=expression.false())
    denominator: Mapped[bool] = mapped_column(default=False, server_default=expression.false())


class Professions(Base):
    __tablename__ = "professions"

    id: Mapped[my_id]
    weekly_day: Mapped[Days]
    teacher_id: Mapped[int] = mapped_column(ForeignKey("person.id", ondelete="CASCADE"))
    group_id: Mapped[int] = mapped_column(ForeignKey("group.id", ondelete="CASCADE"))
    item_id: Mapped[int] = mapped_column(ForeignKey("item.id", ondelete="CASCADE"))
    number_couple: Mapped[int]
    distance: Mapped[bool] = mapped_column(default=False, server_default=expression.false())
    denominator: Mapped[bool] = mapped_column(default=False, server_default=expression.false())


class Substitutions_Specialties(Base):
    __tablename__ = "substitutions_specialties"

    id: Mapped[int] = mapped_column(ForeignKey("specialties.id", ondelete="CASCADE"), primary_key=True)
    weekly_day: Mapped[Days]
    teacher_id: Mapped[int] = mapped_column(ForeignKey("person.id", ondelete="CASCADE"))
    group_id: Mapped[int] = mapped_column(ForeignKey("group.id", ondelete="CASCADE"))
    item_id: Mapped[int] = mapped_column(ForeignKey("item.id", ondelete="CASCADE"))
    number_couple: Mapped[int]
    distance: Mapped[bool] = mapped_column(default=False, server_default=expression.false())
    denominator: Mapped[bool] = mapped_column(default=False, server_default=expression.false())


class Substitutions_Professions(Base):
    __tablename__ = "substitutions_professions"

    id: Mapped[int] = mapped_column(ForeignKey("professions.id", ondelete="CASCADE"), primary_key=True)
    weekly_day: Mapped[Days]
    teacher_id: Mapped[int] = mapped_column(ForeignKey("person.id", ondelete="CASCADE"))
    group_id: Mapped[int] = mapped_column(ForeignKey("group.id", ondelete="CASCADE"))
    item_id: Mapped[int] = mapped_column(ForeignKey("item.id", ondelete="CASCADE"))
    number_couple: Mapped[int]
    distance: Mapped[bool] = mapped_column(default=False, server_default=expression.false())
    denominator: Mapped[bool] = mapped_column(default=False, server_default=expression.false())
