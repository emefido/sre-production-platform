import os


class Settings:
    APP_ENV = os.getenv("APP_ENV", "local")

    DATABASE_HOST = os.getenv("DATABASE_HOST")
    DATABASE_PORT = int(os.getenv("DATABASE_PORT", "5432"))
    DATABASE_NAME = os.getenv("DATABASE_NAME")
    DATABASE_USER = os.getenv("DATABASE_USER")
    DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")

    REDIS_HOST = os.getenv("REDIS_HOST")
    REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))


settings = Settings()