from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import companies, compute, results
from .utils.logger import get_logger

# Initialize Logger
logger = get_logger("backend")

# Initialize FastAPI Application
app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://frontend-service-91173979159.europe-west3.run.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(companies.router, prefix="/api", tags=["companies"])
app.include_router(compute.router, prefix="/api", tags=["compute"])
app.include_router(results.router, prefix="/api", tags=["results"])


# Health Check Endpoint
@app.get("/api/health", tags=["health"])
async def health_check():
    return {"status": "Healthy"}


logger.info("Application startup complete.")

# Main entry point for local running
if __name__ == "__main__":
    import uvicorn
    import os

    port = int(os.getenv("PORT", 8085))
    logger.info(f"Starting application on port {port}...")
    uvicorn.run(app, host="0.0.0.0", port=port)
