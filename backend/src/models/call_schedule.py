
from datetime import datetime
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.sql import expression
from database import Base



class Time_Couple(Base):
    __tablename__ = "time_couple"

    number_couple: Mapped[int] = mapped_column(primary_key=True)
    start_time: Mapped[str]
    end_time: Mapped[str]


class Saturday_Time_Couple(Base):
    __tablename__ = "saturday_time_couple"

    number_couple: Mapped[int] = mapped_column(primary_key=True)
    start_time: Mapped[str]
    end_time: Mapped[str]


class Change_Time_Couple(Base):
    __tablename__ = "change_time_couple"

    start_date: Mapped[datetime]
    end_date: Mapped[datetime]
    number_couple: Mapped[int] = mapped_column(primary_key=True)
    start_time: Mapped[str]
    end_time: Mapped[str]
    saturday: Mapped[bool] = mapped_column(default=False, server_default=expression.false())
    all_days: Mapped[bool] = mapped_column(default=False, server_default=expression.false())
