from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI(
    title="SRE Production Platform API",
    description="Core API service for the SRE Production Platform.",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "service": "api-service",
        "status": "running",
        "message": "SRE Production Platform API",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/live")
def live():
    return {
        "status": "alive",
    }


@app.get("/ready")
def ready():
    return {
        "status": "ready",
    }
