from fastapi import APIRouter
from typing import List
from app.database.db import DB
from app.models.response_models import SavedResult

router = APIRouter()


@router.get("/fetch-saved-results", response_model=List[SavedResult])
def list_saved_results():
    """
    List all saved results from the simulated data store.
    """
    return DB.list_results()


@router.post("/save-results", response_model=str)
def save_result(result: SavedResult):
    """
    Save a new result to the simulated data store and return its unique ID.
    """
    result_id = DB.save_result(result.dict(exclude={"id"}))
    return result_id
