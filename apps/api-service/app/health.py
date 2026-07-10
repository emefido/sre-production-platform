from datetime import datetime, timezone

from app.cache import check_redis
from app.database import check_postgres


def readiness_check():
    postgres_status = "healthy"
    redis_status = "healthy"

    try:
        check_postgres()
    except Exception as e:
        postgres_status = f"unhealthy: {e}"

    try:
        check_redis()
    except Exception as e:
        redis_status = f"unhealthy: {e}"

    overall_status = (
        "ready"
        if postgres_status == "healthy" and redis_status == "healthy"
        else "not_ready"
    )

    return {
        "status": overall_status,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "dependencies": {
            "postgres": postgres_status,
            "redis": redis_status,
        },
    }