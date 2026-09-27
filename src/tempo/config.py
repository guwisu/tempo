import os

from pydantic_settings import BaseSettings, SettingsConfigDict

from pathlib import Path

class Settings(BaseSettings):
    DB_HOST: str | None = None
    DB_PORT: int | None = None
    DB_USER: str | None = None
    DB_PASS: str | None = None
    DB_NAME: str | None = None

    @property
    def database_url(self):
        if all([self.DB_HOST, self.DB_USER, self.DB_PASS, self.DB_NAME]):
            return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

        home_dir = Path.home() / ".tempo"
        home_dir.mkdir(exist_ok=True)
        return f"sqlite:///{home_dir}/tempo.db"

    model_config = SettingsConfigDict(
        env_file=f"{Path(__file__).parent.parent.parent / '.env'}",
        env_ignore_empty=True,
        extra="ignore"
        )

settings = Settings()