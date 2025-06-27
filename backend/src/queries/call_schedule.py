from schemas import *
from db import *
from models import *

from datetime import datetime

from typing import Union

from sqlalchemy import select


async def get_time_couple(number_couple: Union[int, None] = None) -> list[Time_CoupleGet]:
    async with Session() as session:
        query = (
            select(Time_Couple)
            .where(
                (Time_Couple.number_couple == number_couple if number_couple != None else True)
            )
        )

        res = await session.execute(query)
        result_orm = res.scalars().all()

        result_dto = [Time_CoupleGet.model_validate(time_couple, from_attributes=True) for time_couple in result_orm]
        return result_dto


async def get_saturday_time_couple(number_couple: Union[int, None] = None) -> list[Saturday_Time_CoupleGet]:
    async with Session() as session:
        query = (
            select(Saturday_Time_Couple)
            .where(
                (Saturday_Time_Couple.number_couple == number_couple if number_couple != None else True)
            )
        )

        res = await session.execute(query)
        result_orm = res.scalars().all()

        result_dto = [Saturday_Time_CoupleGet.model_validate(time_couple, from_attributes=True) for time_couple in result_orm]
        return result_dto


async def get_change_time_couple(date: Union[datetime, None] = None, number_couple: Union[int, None] = None) -> list[Change_Time_CoupleGet]:
    async with Session() as session:
        query = (
            select(Change_Time_Couple)
            .where(
                (Change_Time_Couple.number_couple == number_couple if number_couple != None else True),
                (Change_Time_Couple.start_date <= date and date <= Change_Time_Couple.end_date if date != None else True)
            )
        )

        res = await session.execute(query)
        result_orm = res.scalars().all()

        result_dto = [Change_Time_CoupleGet.model_validate(time_couple, from_attributes=True) for time_couple in result_orm]
        return result_dto
