import redis

from app.config import settings


redis_client = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    socket_connect_timeout=3,
)


def check_redis():
    redis_client.ping()