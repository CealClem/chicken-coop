import datetime
from enum import IntEnum
from typing import Optional
from pydantic import BaseModel, Field


class TimeOfDay(IntEnum):
    MORNING = 0
    EVENING = 1

class Assignment(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    user_id: str
    date: datetime.datetime
    time_of_day: TimeOfDay

    model_config = {"populate_by_name": True}
