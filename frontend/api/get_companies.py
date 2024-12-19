import requests
from api.config import settings


def get_companies():
    resp = requests.get(f"{settings.API_URL}/companies")
    if resp.status_code == 200:
        return resp.json().get("companies", [])
    else:
        return []
