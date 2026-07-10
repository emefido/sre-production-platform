import logging
import time

from starlette.middleware.base import BaseHTTPMiddleware

logger = logging.getLogger("sre-platform")


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start_time = time.time()

        response = await call_next(request)

        duration = (time.time() - start_time) * 1000

        logger.info(
            "%s %s %s %.2fms",
            request.method,
            request.url.path,
            response.status_code,
            duration,
        )

        return response