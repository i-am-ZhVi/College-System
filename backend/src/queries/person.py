from schemas import *
from db import *
from models import *

from typing import Union

from sqlalchemy.orm import selectinload
from sqlalchemy import select

async def get_persons(id: Union[int, None] = None, login_id: Union[int, None] = None, surname: Union[str, None] = None,
    name: Union[str, None] = None, patronymic: Union[str, None] = None,
    phone: Union[str, None] = None, role: Union[Role, None] = None) -> list[PersonGet]:

    async with Session() as session:

            query = (
                select(Person)
                .where(
                    (Person.id == id if id != None else True),
                    (Person.login_id == login_id if login_id != None else True),
                    (Person.surname == surname if surname != None else True),
                    (Person.name == name if name != None else True),
                    (Person.patronymic == patronymic if patronymic != None else True),
                    (Person.phone == phone if phone != None else True),
                    (Person.role == role if role != None else True)
                )
            )


            res = await session.execute(query)
            result_orm = res.scalars().all()


            result_dto = [PersonGet.model_validate(person, from_attributes=True) for person in result_orm]
            return result_dto


async def get_persons_rel(id: Union[int, None] = None, login_id: Union[int, None] = None, surname: Union[str, None] = None,
    name: Union[str, None] = None, patronymic: Union[str, None] = None,
    phone: Union[str, None] = None, role: Union[Role, None] = None) -> list[PersonRel] | None:
    async with Session() as session:
            query = (
                select(Person)
                .options(
                    selectinload(Person.channels),
                    selectinload(
                    Person.chats),selectinload(
                    Person.teacher_posts),selectinload(
                    Person.icon),selectinload(
                    Person.teacher_groups),selectinload(
                    Person.student_groups),selectinload(
                    Person.specialties),selectinload(
                    Person.professions_i),selectinload(
                    Person.substitutions_specialties),selectinload(
                    Person.substitutions_professions))
                .where(
                    (Person.id == id if id != None else True),
                    (Person.login_id == login_id if login_id != None else True),
                    (Person.surname == surname if surname != None else True),
                    (Person.name == name if name != None else True),
                    (Person.patronymic == patronymic if patronymic != None else True),
                    (Person.phone == phone if phone != None else True),
                    (Person.role == role if role != None else True)
                )
            )

            res = await session.execute(query)
            result_orm = res.scalars().all()


            result_dto = [PersonRel.model_validate(person, from_attributes=True) for person in result_orm]
            return result_dto
