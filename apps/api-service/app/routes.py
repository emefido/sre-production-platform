from datetime import datetime, timezone

from fastapi import APIRouter
from fastapi.responses import Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

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


@router.get("/metrics")
def metrics():
    return Response(
        generate_latest(),
        media_type=CONTENT_TYPE_LATEST,
    )