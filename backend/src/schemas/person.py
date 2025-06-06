from pydantic import BaseModel

from models.person import Role

class LoginPost(BaseModel):
    login: str
    password: str


class LoginGet(LoginPost):
    id: int


class PersonPost(BaseModel):
    login_id: int
    icon_id: int
    surname: str
    name: str
    patronymic: str | None
    phone: str | None
    role: Role

class PersonGet(PersonPost):
    id: int
