import requests
import datetime
from api.config import settings


def save_result(company: str, start_date: datetime.date, results: dict):
    payload = {
        "id": "",
        "company": company,
        "start_date": start_date.isoformat(),
        "series_only": results.get("series_only"),
        "series_with_strings": results.get("series_with_strings"),
    }
    try:
        api_url = f"{settings.BACKEND_URL}/api/save-results"
        res = requests.post(api_url, json=payload)

        if res.status_code != 200:
            print(f"Error saving results: {res.text}")
            return None

        return res.text
    except requests.exceptions.RequestException as e:
        print(f"Error saving results: {e}")
        return None
