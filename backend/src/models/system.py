import enum

#from models.person import Person

from typing import Annotated
from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import expression
from sqlalchemy.sql.schema import ForeignKey
from database import Base
from datetime import datetime

my_id = Annotated[int, mapped_column(primary_key=True)]

class Post(Base):
    __tablename__ = "post"

    id: Mapped[my_id]
    name: Mapped[str]

    teachers: Mapped[list["Person"]] = relationship(
        back_populates="teacher_posts",
        secondary="teacher"
    )

    items: Mapped[list["Item"]] = relationship(
        back_populates="post"
    )


class Teacher(Base):
    __tablename__ = "teacher"

    person_id: Mapped[int] = mapped_column(ForeignKey("person.id", ondelete="CASCADE"), primary_key=True)
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id", ondelete="CASCADE"), primary_key=True)


class Item(Base):
    __tablename__ = "item"

    id: Mapped[my_id]
    name: Mapped[str]
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id", ondelete="CASCADE"))

    post: Mapped["Post"] = relationship(
        back_populates="items"
    )

    grades: Mapped[list["Grade"]] = relationship(
        back_populates="item"
    )

    groups: Mapped[list["Group"]] = relationship(
        back_populates="items",
        secondary="item_for_group"
    )

    specialties: Mapped[list["Specialties"]] = relationship(
        back_populates="item"
    )

    substitutions_specialties: Mapped[list["Substitutions_Specialties"]] = relationship(
        back_populates="item"
    )

    professions_i: Mapped[list["Professions"]] = relationship(
        back_populates="item"
    )

    substitutions_professions: Mapped[list["Substitutions_Professions"]] = relationship(
        back_populates="item"
    )



class Grade(Base):
    __tablename__ = "grade"

    id: Mapped[my_id]
    teacher_id: Mapped[int] = mapped_column(ForeignKey("person.id", ondelete="CASCADE"))
    student_id: Mapped[int] = mapped_column(ForeignKey("person.id", ondelete="CASCADE"))
    item_id: Mapped[int] = mapped_column(ForeignKey("item.id", ondelete="CASCADE"))
    evaluation: Mapped[int] = mapped_column(nullable=True)
    truancy: Mapped[bool] = mapped_column(default=False, server_default=expression.false())
    create_at: Mapped[datetime] = mapped_column(default=datetime.utcnow(), server_default=text("TIMEZONE('utc', now())"))
    update_at: Mapped[datetime] = mapped_column(default=datetime.utcnow(), server_default=text("TIMEZONE('utc', now())"), onupdate=datetime.utcnow())
    number_couple: Mapped[int]

    student: Mapped["Person"] = relationship(
        "Person",
        backref="grades_student",
        foreign_keys=[student_id]

    )

    teacher: Mapped["Person"] = relationship(
        "Person",
        backref="grades_teacher",
        foreign_keys=[teacher_id]
    )

    item: Mapped["Item"] = relationship(
        back_populates="grades"
    )


class Group(Base):
    __tablename__ = "group"

    id: Mapped[my_id]
    name: Mapped[str]
    professions: Mapped[bool] = mapped_column(default=False, server_default=expression.false())
    denominator: Mapped[bool] = mapped_column(default=False, server_default=expression.false())
    start_year: Mapped[datetime] = mapped_column(default=datetime.utcnow(), server_default=text("TIMEZONE('utc', now())"))

    teachers: Mapped[list["Person"]] = relationship(
        back_populates="teacher_groups",
        secondary="teacher_to_group"
    )

    students: Mapped[list["Person"]] = relationship(
        back_populates="teacher_groups",
        secondary="student_to_group"
    )

    items: Mapped[list["Item"]] = relationship(
        back_populates="groups",
        secondary="item_for_group"
    )

    specialties: Mapped[list["Specialties"]] = relationship(
        back_populates="group"
    )

    substitutions_specialties: Mapped[list["Substitutions_Specialties"]] = relationship(
        back_populates="group"
    )

    professions_i: Mapped[list["Professions"]] = relationship(
        back_populates="group"
    )

    substitutions_professions: Mapped[list["Substitutions_Professions"]] = relationship(
        back_populates="group"
    )



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
    tuesday = "Вторник"
    wednesday = "Среда"
    thursday = "Четверг"
    friday = "Пятница"
    saturday = "Суббота"
    sunday = "Воскресенье"


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

    teacher: Mapped["Person"] = relationship(
        back_populates="specialties"
    )

    group: Mapped["Group"] = relationship(
        back_populates="specialties"
    )

    item: Mapped["Item"] = relationship(
        back_populates="specialties"
    )


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

    teacher: Mapped["Person"] = relationship(
        back_populates="professions_i"
    )

    group: Mapped["Group"] = relationship(
        back_populates="professions_i"
    )

    item: Mapped["Item"] = relationship(
        back_populates="professions_i"
    )



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

    teacher: Mapped["Person"] = relationship(
        back_populates="substitutions_specialties"
    )

    group: Mapped["Group"] = relationship(
        back_populates="substitutions_specialties"
    )

    item: Mapped["Item"] = relationship(
        back_populates="substitutions_specialties"
    )


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

    teacher: Mapped["Person"] = relationship(
        back_populates="substitutions_professions"
    )

    group: Mapped["Group"] = relationship(
        back_populates="substitutions_professions"
    )

    item: Mapped["Item"] = relationship(
        back_populates="substitutions_professions"
    )
