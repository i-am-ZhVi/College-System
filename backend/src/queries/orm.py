import asyncio

from sqlalchemy import text, insert
from database import Base, engine, session
from models import Person



async def update_tables():
    engine.echo = False

    async with engine.connect() as conn:
        #await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        await conn.commit()

    engine.echo = True
