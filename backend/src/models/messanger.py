import enum

from sqlalchemy import text
from sqlalchemy.sql import expression
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy.orm.base import Mapped
from sqlalchemy.schema import ForeignKey
from typing import Annotated
from db import Base
from datetime import datetime

from models.site import News_Page


my_id = Annotated[int, mapped_column(primary_key=True)]

class Chat(Base):
    __tablename__ = "chat"

    id: Mapped[my_id]
    icon_id: Mapped[int] = mapped_column(ForeignKey("file.id"), nullable=True)
    creator_id: Mapped[int] = mapped_column(ForeignKey("person.id", ondelete="CASCADE"))
    name: Mapped[str]
    description: Mapped[str]

    creator: Mapped["Person"] = relationship(
        back_populates="chats"
    )

    subscribers: Mapped[list["Person"]] = relationship(
        back_populates="subscribes_on_chats",
        secondary="subscriber"
    )

    icon: Mapped["File"] = relationship(
        back_populates="chats"
    )




class Channel(Base):
    __tablename__ = "channel"

    id: Mapped[my_id]
    icon_id: Mapped[int] = mapped_column(ForeignKey("file.id"), nullable=True)
    creator_id: Mapped[int] = mapped_column(ForeignKey("person.id", ondelete="CASCADE"))
    name: Mapped[str]
    description: Mapped[str]

    creator: Mapped["Person"] = relationship(
        back_populates="channels"
    )

    subscribers: Mapped[list["Person"]] = relationship(
        back_populates="subscribes_on_channels",
        secondary="subscriber"
    )

    icon: Mapped["File"] = relationship(
        back_populates="channels"
    )


class Subscriber(Base):
    __tablename__ = "subscriber"

    id: Mapped[my_id]
    subscriber_id: Mapped[int] = mapped_column(ForeignKey("person.id", ondelete="CASCADE"))
    person_id: Mapped[int] = mapped_column(ForeignKey("person.id", ondelete="CASCADE"), nullable=True)
    chat_id: Mapped[int] = mapped_column(ForeignKey("chat.id", ondelete="CASCADE"), nullable=True)
    channel_id: Mapped[int] = mapped_column(ForeignKey("channel.id", ondelete="CASCADE"), nullable=True)
    admin: Mapped[bool] = mapped_column(default=False, server_default=expression.false())
    can_write: Mapped[bool] = mapped_column(default=True, server_default=expression.true())


class Message(Base):
    __tablename__ = "message"

    id: Mapped[my_id]
    created_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
    update_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"), onupdate=datetime.utcnow)
    sender_id: Mapped[int] = mapped_column(ForeignKey("person.id"))
    recipient_id: Mapped[int] = mapped_column(ForeignKey("person.id"), nullable=True)
    chat_id: Mapped[int] = mapped_column(ForeignKey("chat.id"), nullable=True)
    channel_id: Mapped[int] = mapped_column(ForeignKey("channel.id"), nullable=True)
    message: Mapped[str] = mapped_column(nullable=True)

    files: Mapped[list["File"]] = relationship(
        back_populates="messages",
        secondary="file_in_message"
    )


class File_Type(enum.Enum):
    image = "image"
    text = "text"
    video = "video"


class File(Base):
    __tablename__ = "file"

    id: Mapped[my_id]
    name: Mapped[str]
    type: Mapped[File_Type] = mapped_column(nullable=True)

    messages: Mapped[list["Message"]] = relationship(
        back_populates="files",
        secondary="file_in_message"
    )

    persons: Mapped[list["Person"]] = relationship(
        back_populates="icon"
    )

    chats: Mapped[list["Chat"]] = relationship(
        back_populates="icon"
    )

    channels: Mapped[list["Channel"]] = relationship(
        back_populates="icon"
    )

    pages: Mapped[list["News_Page"]] = relationship(
        back_populates="files",
        secondary="file_to_main_page"
    )


class File_in_Message(Base):
    __tablename__ = "file_in_message"

    file_id: Mapped[int] = mapped_column(ForeignKey("file.id"), primary_key=True)
    message_id: Mapped[int] = mapped_column(ForeignKey("message.id"), primary_key=True)
