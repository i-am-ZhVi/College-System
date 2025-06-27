
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def create_fastapi_app():
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
    )



    return app


app = create_fastapi_app()
