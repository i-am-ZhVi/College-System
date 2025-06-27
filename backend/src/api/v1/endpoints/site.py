from queries import *
from typing import Union
from fastapi import APIRouter

from api import app

news_router = APIRouter(prefix="/news", tags=["news"])

@news_router.get("/news_pages")
async def api_get_news_pages(id: Union[int, None] = None):
    news_pages = await get_News(id)

    return {
        "data": news_pages
    }


@news_router.get("/news_pagesRelationships")
async def api_get_news_pagesRelationships(id: Union[int, None] = None):
    news_pages = await get_NewsRelationships(id)

    return {
        "data": news_pages
    }


app.include_router(news_router)
