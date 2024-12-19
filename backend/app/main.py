from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import companies, compute, results
from app.utils.logger import get_logger

logger = get_logger("backend")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(companies.router, prefix="/api", tags=["companies"])
app.include_router(compute.router, prefix="/api", tags=["compute"])
app.include_router(results.router, prefix="/api", tags=["results"])

logger.info("Application startup complete.")
