import requests
from api.config import settings


def get_companies():
    try:
        api_url = f"{settings.BACKEND_URL}/api/companies"
        res = requests.get(api_url)

        if res.status_code != 200:
            print(f"Error fetching companies: {res.text}")
            return []

        return res.json().get("companies", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching companies: {str(e)}")
        return []
