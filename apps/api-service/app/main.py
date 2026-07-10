from fastapi import FastAPI

from app.routes import router

app = FastAPI(
    title="SRE Production Platform API",
    description="Core API service for the SRE Production Platform.",
    version="0.1.0",
)

app.include_router(router)