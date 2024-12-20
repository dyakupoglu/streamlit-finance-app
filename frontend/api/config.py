import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    BACKEND_URL: str = os.getenv(
        "BACKEND_URL", "https://backend-service-91173979159.europe-west3.run.app"
    )


settings = Settings()
