from pathlib import Path
from typing import Literal
from pydantic import PostgresDsn

from pydantic_settings import BaseSettings, SettingsConfigDict

PROJECT_DIR = Path(__file__).parents[3].resolve()


class PydanticBaseSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=PROJECT_DIR / ".env", env_file_encoding="utf-8", case_sensitive=False
    )


class AppSettings(PydanticBaseSettings):
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    DB_HOST: str
    DB_PORT: int

    SECRET_KEY: str
    JWT_ALGORYTHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    CLIENT_ID: str
    CLIENT_SECRET: str

    SUPERUSER_LOGIN: str = "admin"
    SUPERUSER_PASS: str = "admin"
    SUPERUSER_EMAIL: str = "example@mail.com"

    @staticmethod
    def build_postgres_url(pg_driver: Literal["psycopg2", "asyncpg"], **values):
        url = PostgresDsn.build(
            scheme="postgresql+" + pg_driver,
            username=values.get("DB_USER"),
            password=values.get("DB_PASS"),
            host=values.get("DB_HOST"),
            port=values.get("DB_PORT"),
            path=values.get("DB_NAME"),
        )
        return url

    @property
    def sync_db_url(self):
        return self.build_postgres_url("psycopg2", **self.__dict__)

    @property
    def async_db_url(self):
        return self.build_postgres_url("asyncpg", **self.__dict__)


def get_settings():
    return AppSettings()
