from schemas import *
from db import *
from models import *

async def get_persons() -> list[PersonGet]:

    async with Session() as session:
            query = (
                select(Person)
            )

            res = await session.execute(query)
            result_orm = res.scalars().all()


            result_dto = [PersonGet.model_validate(p, from_attributes=True) for p in result_orm]
            return result_dto

async def get_person(id: int) -> PersonRel | None:
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
                    Person.subscribes_on_channels),selectinload(
                    Person.specialties),selectinload(
                    Person.professions_i),selectinload(
                    Person.substitutions_specialties),selectinload(
                    Person.substitutions_professions),selectinload(
                    Person.subscribes_on_channels),selectinload(
                    Person.subscribes_on_chats))
                .where(Person.id == id)
            )

            res = await session.execute(query)
            result_orm = res.scalars().first()

            if (result_orm == None):
                return None

            result_dto = PersonRel.model_validate(result_orm, from_attributes=True)
            return result_dto
