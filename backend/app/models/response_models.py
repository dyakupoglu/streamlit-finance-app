from pydantic import BaseModel
from typing import List, Dict


class CompanyListResponse(BaseModel):
    companies: List[str]


class ComputationResponse(BaseModel):
    series_with_strings: List[Dict]
    series_only: List[Dict]


class SavedResult(BaseModel):
    id: str
    company: str
    start_date: str
    series_only: List[Dict]
    series_with_strings: List[Dict]
