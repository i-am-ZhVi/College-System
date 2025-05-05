import enum

from typing import Annotated
from sqlalchemy.orm import Mapped, mapped_column, relationship
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
    login_id: Mapped[int] = mapped_column(ForeignKey("login.id", ondelete="CASCADE"))
    icon_id: Mapped[int] = mapped_column(ForeignKey("file.id"), nullable=True)
    surname: Mapped[str]
    name: Mapped[str]
    patronymic: Mapped[str] = mapped_column(nullable=True)
    phone: Mapped[str] = mapped_column(nullable=True)
    role: Mapped[Role] = mapped_column(default=Role.student, server_default="student")

    teacher_posts: Mapped[list["Post"]] = relationship(
        back_populates="teachers",
        secondary="teacher"
    )

    icon: Mapped["File"] = relationship(
        back_populates="persons"
    )

    teacher_groups: Mapped[list["Group"]] = relationship(
        back_populates="teachers",
        secondary="teacher_to_group"
    )

    student_groups: Mapped[list["Group"]] = relationship(
        back_populates="students",
        secondary="student_to_group"
    )

    specialties: Mapped[list["Specialties"]] = relationship(
        back_populates="teacher"
    )

    substitutions_specialties: Mapped[list["Substitutions_Specialties"]] = relationship(
        back_populates="teacher"
    )

    professions_i: Mapped[list["Professions"]] = relationship(
        back_populates="teacher"
    )

    substitutions_professions: Mapped[list["Substitutions_Professions"]] = relationship(
        back_populates="teacher"
    )

    chats: Mapped[list["Chat"]] = relationship(
        back_populates="creator"
    )

    channels: Mapped[list["Channel"]] = relationship(
        back_populates="creator"
    )

    subscribes_on_chats: Mapped[list["Chat"]] = relationship(
        back_populates="subscribers",
        secondary="subscriber"
    )

    subscribes_on_channels: Mapped[list["Channel"]] = relationship(
        back_populates="subscribers",
        secondary="subscriber"
    )







class Login(Base):
    __tablename__ = "login"

    id: Mapped[my_id]
    login: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
