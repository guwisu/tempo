import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg://postgres:postgres@localhost:5432/postgres"
        )


settings = Settings()