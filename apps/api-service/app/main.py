from fastapi import FastAPI

from app.logging_config import setup_logging
from app.middleware import RequestLoggingMiddleware
from app.routes import router

setup_logging()

app = FastAPI(
    title="SRE Production Platform API",
    description="Core API service for the SRE Production Platform.",
    version="0.1.0",
)

app.add_middleware(RequestLoggingMiddleware)

app.include_router(router)