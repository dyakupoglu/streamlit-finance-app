import requests
from api.config import settings


def fetch_saved_results():
    try:
        api_url = f"{settings.BACKEND_URL}/api/fetch-saved-results"
        res = requests.get(api_url)

        if res.status_code != 200:
            print(f"Error fetching saved results: {res.text}")
            return []

        return res.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching saved results: {e}")
        return []
