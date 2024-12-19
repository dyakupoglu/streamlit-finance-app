import requests
import datetime
from api.config import settings


def compute_results(company: str, start_date: datetime.date, values: list[float]):
    payload = {
        "company": company,
        "start_date": start_date.isoformat(),
        "values": values,
    }
    resp = requests.post(f"{settings.API_URL}/compute", json=payload)
    if resp.status_code == 200:
        return resp.json()
    else:
        return None
