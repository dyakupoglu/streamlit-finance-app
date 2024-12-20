import requests
import datetime
from api.config import settings


def compute_results(company: str, start_date: datetime.date, values: list[float]):
    payload = {
        "company": company,
        "start_date": start_date.isoformat(),
        "values": values,
    }
    try:
        api_url = f"{settings.BACKEND_URL}/api/compute"
        res = requests.post(api_url, json=payload)

        if res.status_code != 200:
            print(f"Error computing results: {res.text}")
            return None

        return res.json()
    except requests.exceptions.RequestException as e:
        print(f"Error computing results: {e}")
        return None
