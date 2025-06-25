from typing_extensions import Optional
from pydantic import BaseModel
from datetime import datetime

from models.messanger import File_Type

class ChatPost(BaseModel):
    icon_id: int | None
    creator_id: int
    name: str
    description: str

class ChatGet(ChatPost):
    id: int

class ChatRel(ChatGet):
    creator: "PersonGet"
    icon: Optional["FileGet"] = None


class ChannelPost(BaseModel):
    icon_id: int | None
    creator_id: int
    name: str
    description: str

class ChannelGet(ChannelPost):
    id: int

class ChannelRel(ChannelGet):
    creator: "PersonGet"
    icon: "FileGet"


class SubscriberPost(BaseModel):
    subrscriber_id: int
    person_id: int | None
    chat_id: int | None
    channel_id: int | None
    admin: bool
    can_write: bool

class SubscriberGet(SubscriberPost):
    id: int


class MessagePost(BaseModel):
    sender_id: int
    recipient_id: int | None
    chat_id: int | None
    channel_id: int | None
    message: int | None

class MessageGet(MessagePost):
    id: int
    created_at: datetime
    update_at: datetime

class MessageRel(MessageGet):
    files: list["FileGet"]


class FilePost(BaseModel):
    name: str
    type: File_Type

class FileGet(FilePost):
    id: int

class FileRel(FileGet):
    messages: list["MessageGet"]
    persons: list["PersonGet"]
    chats: list["ChatGet"]
    channels: list["ChannelGet"]
    pages: list["News_PageGet"]


class File_in_MessagePost(BaseModel):
    file_id: int
    message_id: int

class File_in_MessageGet(File_in_MessagePost):
    pass
