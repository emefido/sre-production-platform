from datetime import datetime, timezone

from fastapi import APIRouter

from app.health import readiness_check

router = APIRouter()


@router.get("/")
def root():
    return {
        "service": "api-service",
        "status": "running",
        "message": "SRE Production Platform API",
    }


@router.get("/health")
def health():
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@router.get("/live")
def live():
    return {
        "status": "alive",
    }


@router.get("/ready")
def ready():
    return readiness_check()