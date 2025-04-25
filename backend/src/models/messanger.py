from sqlalchemy.orm import mapped_column
from sqlalchemy.orm.base import Mapped
from sqlalchemy.schema import ForeignKey
from typing import Annotated
from database import Base


my_id = Annotated[int, mapped_column(primary_key=True)]

class Chat(Base):
    __tablename__ = "chat"

    id: Mapped[my_id]
    icon_path: Mapped[str] = mapped_column(nullable=True)
    creator_id: Mapped[int] = mapped_column(ForeignKey("person.id", ondelete="CASCADE"))
    name: Mapped[str]
    description: Mapped[str]

class Channel(Base):
    __tablename__ = "channel"

    id: Mapped[my_id]
    icon_path: Mapped[str] = mapped_column(nullable=True)
    creator_id: Mapped[int] = mapped_column(ForeignKey("person.id", ondelete="CASCADE"))
    name: Mapped[str]
    description: Mapped[str]



class Subscriber(Base):
    __tablename__ = "subscriber"

    person_id: Mapped[int] = mapped_column(ForeignKey("person.id", ondelete="CASCADE"), primary_key=True)
    chat_id: Mapped[int] = mapped_column(ForeignKey("chat.id", ondelete="CASCADE"), primary_key=True)
    channel_id: Mapped[int] = mapped_column(ForeignKey("channel.id", ondelete="CASCADE"), primary_key=True)
    admin: Mapped[bool] = mapped_column(default=False)
    can_write: Mapped[bool] = mapped_column(default=True)


class Message(Base):
    __tablename__ = "message"

    id: Mapped[my_id]
    id_chat_message: Mapped[int]
    sender_id: Mapped[int] = mapped_column(ForeignKey("person.id"))
    recipient_id: Mapped[int] = mapped_column(ForeignKey("person.id"), nullable=True)
    chat_id: Mapped[int] = mapped_column(ForeignKey("chat.id"), nullable=True)
    channel_id: Mapped[int] = mapped_column(ForeignKey("channel.id"), nullable=True)
    message: Mapped[str]




class File_Type(Base):
    __tablename__ = "file_type"

    id: Mapped[my_id]
    type: Mapped[str]


class File(Base):
    __tablename__ = "file"

    id: Mapped[my_id]
    message_id: Mapped[int] = mapped_column(ForeignKey("message.id", ondelete="CASCADE"))
    path: Mapped[str]
    type_id: Mapped[int] = mapped_column(ForeignKey("file_type.id", ondelete="CASCADE"))
