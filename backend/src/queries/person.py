from schemas import *
from db import *
from models import *

from sqlalchemy.orm import selectinload
from sqlalchemy import select

async def get_persons() -> list[PersonGet]:

    async with Session() as session:
            query = (
                select(Person)
            )

            res = await session.execute(query)
            result_orm = res.scalars().all()


            result_dto = [PersonGet.model_validate(p, from_attributes=True) for p in result_orm]
            print(result_dto)
            return result_dto


async def get_persons_rel() -> list[PersonRel] | None:
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
            )

            res = await session.execute(query)
            result_orm = res.scalars().all()

            if (result_orm == None):
                return None

            result_dto = [PersonRel.model_validate(p, from_attributes=True) for p in result_orm]
            return result_dto
