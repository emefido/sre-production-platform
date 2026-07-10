from psycopg2.pool import SimpleConnectionPool

from app.config import settings

pool = SimpleConnectionPool(
    minconn=1,
    maxconn=10,
    host=settings.DATABASE_HOST,
    port=settings.DATABASE_PORT,
    dbname=settings.DATABASE_NAME,
    user=settings.DATABASE_USER,
    password=settings.DATABASE_PASSWORD,
)


def check_postgres():
    conn = pool.getconn()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT 1;")
    finally:
        pool.putconn(conn)