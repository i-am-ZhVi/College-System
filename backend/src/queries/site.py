from schemas import *
from db import *
from models import *

from typing import Union

from sqlalchemy.orm import selectinload
from sqlalchemy import select



async def get_News(id: Union[int, None] = None) -> list[News_PageGet]:
    async with Session() as session:
        query = (
            select(News_Page)
            .where(
                (News_Page.id == id if id != None else True)
            )
        )

        res = await session.execute(query)
        result_orm = res.scalars().all()


        result_dto = [News_PageGet.model_validate(news, from_attributes=True) for news in result_orm]
        return result_dto


async def get_NewsRelationships(id: Union[int, None] = None) -> list[News_PageGet]:
    async with Session() as session:
        query = (
            select(News_Page)
            .where(
                (News_Page.id == id if id != None else True)
            )
            .options(
                selectinload(News_page.files)
            )
        )

        res = await session.execute(query)
        result_orm = res.scalars().all()

        result_dto = [News_PageGet.model_validate(news, from_attributes=True) for news in result_orm]
        return result_dto
