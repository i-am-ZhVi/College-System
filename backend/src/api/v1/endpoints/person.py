from fastapi.routing import APIRouter
from queries import *
from typing import Union

from api import app


persons_router = APIRouter(prefix="/person", tags=["persons"])



@persons_router.post("/new_person")
async def api_post_person(person: PersonPost):
    return person


@persons_router.get("/personsRelationships")
async def api_get_persons_rel(id: Union[int, None] = None, login_id: Union[int, None] = None, surname: Union[str, None] = None,
    name: Union[str, None] = None, patronymic: Union[str, None] = None,
    phone: Union[str, None] = None, role: Union[Role, None] = None):
    persons = await get_persons_rel(id=id, login_id=login_id, surname=surname,
        name=name, patronymic=patronymic, phone=phone, role=role)

    response = {
        "data": persons
    }
    return response

@persons_router.get("/persons")
async def api_get_persons(id: Union[int, None] = None, login_id: Union[int, None] = None, surname: Union[str, None] = None,
    name: Union[str, None] = None, patronymic: Union[str, None] = None,
    phone: Union[str, None] = None, role: Union[Role, None] = None):
    person = await get_persons(id=id, login_id=login_id, surname=surname,
        name=name, patronymic=patronymic, phone=phone, role=role)

    response = {
        "data": person
    }

    return response


app.include_router(persons_router)
