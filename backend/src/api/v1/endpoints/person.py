from queries import *
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def create_fastapi_app():
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
    )

    @app.get("/")
    async def api_main():
        return "hello"

    @app.get("/persons")
    async def api_get_persons():
        persons = await get_persons()

        response = {
            "data": persons
        }
        return response

    @app.get("/person")
    async def api_get_person(id: int):
        person = await get_person(id)

        response = {
            "data": person
        }

        return response

    return app
