from fastapi import APIRouter
from app.models.response_models import CompanyListResponse

router = APIRouter()


@router.get("/companies", response_model=CompanyListResponse)
def get_companies():
    """
    Return a list of companies.
    """
    return CompanyListResponse(
        companies=["Company A", "Company B", "Company C", "Slow Company"]
    )
