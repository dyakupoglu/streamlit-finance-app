import requests
from api.config import settings


def fetch_saved_results():
    resp = requests.get(f"{settings.API_URL}/fetch-results")
    if resp.status_code == 200:
        return resp.json()
    else:
        return []
