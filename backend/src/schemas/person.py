from typing_extensions import Optional
from pydantic import BaseModel

from models.person import Role

class LoginPost(BaseModel):
    login: str
    password: str


class LoginGet(LoginPost):
    id: int


class PersonPost(BaseModel):
    login_id: int
    icon_id: int | None
    surname: str
    name: str
    patronymic: str | None
    phone: str | None
    role: Role

class PersonGet(PersonPost):
    id: int


class PersonRel(PersonGet):
    teacher_posts: list["PostGet"]
    icon: Optional["FileGet"] = None
    teacher_groups: list["GroupGet"]
    strudent_groups: Optional[list["GroupGet"]] = None
    specialties: list["SpecialtiesGet"]
    substitutions_specialties: list["Substitutions_SpecialtiesGet"]
    professions_i: list["ProfessionsGet"]
    substitutions_professions: list["Substitutions_ProfessionsGet"]
    chats: list["ChatGet"]
    channels: list["ChannelGet"]
    subscribes_on_chats: list["ChatGet"]
    subscribes_on_channels: list["ChannelGet"]
