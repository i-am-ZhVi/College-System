
from sqlalchemy.ext.asyncio import AsyncAttrs, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase #, mapped_column, Mapped
from config import settings


engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=False,
    #pool_size=5,
    #max_overflow=10
)


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True


session = async_sessionmaker(engine)
