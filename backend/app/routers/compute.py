from fastapi import APIRouter
from app.models.request_models import ComputeRequest
from app.models.response_models import ComputationResponse
from app.utils.utils import generate_random_series
import time

router = APIRouter()


@router.post("/compute", response_model=ComputationResponse)
async def compute(data: ComputeRequest):
    """
    Simulate a long-running computation and return a random series.
    """
    if data.company == "Slow Company":
        time.sleep(240)  # 4 minutes
    else:
        time.sleep(2)

    series_only, series_with_strings = generate_random_series(data.start_date)
    return ComputationResponse(
        series_with_strings=series_with_strings, series_only=series_only
    )
