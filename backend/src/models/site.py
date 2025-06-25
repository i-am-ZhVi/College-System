from datetime import datetime
from typing import Annotated
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy.orm.properties import ForeignKey
from sqlalchemy.sql import expression
from db import Base

my_id = Annotated[int, mapped_column(primary_key=True)]

class News_Page(Base):
    __tablename__ = "news_page"

    id: Mapped[my_id]
    message: Mapped[str] = mapped_column(nullable=True)

    files: Mapped[list["File"]] = relationship(
        back_populates="pages",
        secondary="file_to_main_page"
    )


class File_to_Main_Page(Base):
    __tablename__ = "file_to_main_page"

    news_id: Mapped[int] = mapped_column(ForeignKey("news_page.id"), primary_key=True)
    file_id: Mapped[int] = mapped_column(ForeignKey("file.id"), primary_key=True)
