import os

from dataclasses import dataclass


@dataclass
class Settings():
    DB_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg://postgres:postgres@localhost:5432/postgres"
        )


settings = Settings()