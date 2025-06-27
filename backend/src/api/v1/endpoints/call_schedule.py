from queries import *
from typing import Union
from fastapi import APIRouter

from api import app
from queries.call_schedule import get_change_time_couple, get_saturday_time_couple, get_time_couple

time_couple_router = APIRouter(prefix="/time_couple", tags=["time_couple"])

@time_couple_router.get("/time_couple")
async def api_get_time_couple(number_couple: Union[int, None] = None):
    time_couple = await get_time_couple(number_couple=number_couple)

    return {
        "data": time_couple
    }


@time_couple_router.get("/saturday_time_couple")
async def api_get_saturday_time_couple(number_couple: Union[int, None] = None):
    time_couple = await get_saturday_time_couple(number_couple=number_couple)

    return {
        "data": time_couple
    }


@time_couple_router.get("/change_time_couple")
async def api_get_change_time_couple(date: Union[datetime, None] = None, number_couple: Union[int, None] = None):
    time_couple = await get_change_time_couple(date=date, number_couple=number_couple)

    return {
        "data": time_couple
    }


app.include_router(time_couple_router)
