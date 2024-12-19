import requests
import datetime
from api.config import settings


def save_result(company: str, start_date: datetime.date, results: dict):
    payload = {
        "id": "",
        "company": company,
        "start_date": start_date.isoformat(),
        "series_only": results["series_only"],
        "series_with_strings": results["series_with_strings"],
    }
    resp = requests.post(f"{settings.API_URL}/save-results", json=payload)
    if resp.status_code == 200:
        return resp.text
    else:
        return None
