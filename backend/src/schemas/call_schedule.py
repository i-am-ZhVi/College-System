from pydantic import BaseModel
from datetime import datetime


class Time_CouplePost(BaseModel):
    number_couple: int
    start_time: str
    end_time: str

class Time_CoupleGet(BaseModel):
    pass

class Saturday_Time_CouplePost(BaseModel):
    number_couple: int
    start_time: str
    end_time: str

class Saturday_Time_CoupleGet(Saturday_Time_CouplePost):
    pass


class Change_Time_CouplePost(BaseModel):
    start_date: datetime
    end_date: datetime
    number_couple: int
    start_time: str
    end_time: str
    saturday: bool
    all_days: bool

class Change_Time_CoupleGet(Change_Time_CouplePost):
    pass
