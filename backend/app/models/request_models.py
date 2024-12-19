from pydantic import BaseModel
from typing import List
import datetime


class ComputeRequest(BaseModel):
    company: str
    start_date: datetime.date
    values: List[float]
