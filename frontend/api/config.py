import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    API_URL: str = os.getenv("API_URL", "http://localhost:8080/api")


settings = Settings()
