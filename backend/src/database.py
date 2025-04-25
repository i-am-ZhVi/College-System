
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from config import settings


engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=False,
    #pool_size=5,
    #max_overflow=10
)


class Base(DeclarativeBase):
    pass


session = async_sessionmaker(engine)
