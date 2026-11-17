import os
from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI(
    title="TMX Golden Path Starter Service",
    description="Production-hardened Python microservice boilerplate for Red Hat Developer Hub",
    version="1.0.0",
)

class HealthResponse(BaseModel):
    status: str
    service: str
    version: str

@app.get("/", status_code=status.HTTP_200_OK)
def get_root():
    return {
        "message": "Welcome to TMX Golden Path Service",
        "service": os.getenv("APP_NAME", "tmx-starter-service"),
        "status": "online",
        "docs_url": "/docs",
    }

@app.get("/healthz", response_model=HealthResponse, status_code=status.HTTP_200_OK)
def get_liveness():
    """Liveness probe: verifies the service process is alive and responding."""
    return HealthResponse(
        status="healthy",
        service=os.getenv("APP_NAME", "tmx-starter-service"),
        version="1.0.0",
    )

@app.get("/ready", response_model=HealthResponse, status_code=status.HTTP_200_OK)
def get_readiness():
    """Readiness probe: verifies the service is initialized and ready to receive traffic."""
    return HealthResponse(
        status="ready",
        service=os.getenv("APP_NAME", "tmx-starter-service"),
        version="1.0.0",
    )
