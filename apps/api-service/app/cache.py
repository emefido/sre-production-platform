import redis

from app.config import settings

pool = redis.ConnectionPool(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    max_connections=10,
    decode_responses=True,
)

redis_client = redis.Redis(connection_pool=pool)


def check_redis():
    redis_client.ping()