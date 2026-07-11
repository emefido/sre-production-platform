from fastapi import FastAPI

from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

from app.logging_config import setup_logging
from app.middleware import RequestLoggingMiddleware
from app.routes import router

setup_logging()

resource = Resource.create(
    {
        "service.name": "sre-api",
        "deployment.environment": "local",
    }
)

tracer_provider = TracerProvider(resource=resource)

span_exporter = OTLPSpanExporter(
    endpoint="http://tempo:4318/v1/traces"
)

tracer_provider.add_span_processor(
    BatchSpanProcessor(span_exporter)
)

trace.set_tracer_provider(tracer_provider)

app = FastAPI(
    title="SRE Production Platform API",
    description="Core API service for the SRE Production Platform.",
    version="0.1.0",
)

app.add_middleware(RequestLoggingMiddleware)

app.include_router(router)

FastAPIInstrumentor.instrument_app(app)
