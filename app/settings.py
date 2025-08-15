from pathlib import Path
from sys import prefix

from pydantic import PostgresDsn, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict

_BASE_DIR = Path(prefix).parent.joinpath(".env").resolve().as_posix()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=_BASE_DIR,
        env_file_encoding="utf-8",
        env_ignore_empty=True,
    )
    DEBUG: bool = False

    """Security"""
    OTP_EXPIRES_MINUTES: int = 10
    OTP_MAX_ATTEMPTS: int = 3
    OTP_LENGTH: int = 6
    TOKEN_TYPE: str = "Bearer"
    TOKEN_ALGORITHM: str = "HS256"
    REFRESH_TOKEN_EXPIRES_DAYS: int = 30
    REFRESH_TOKEN_SECRET: str
    ACCESS_TOKEN_EXPIRES_MINUTES: int = 10
    ACCESS_TOKEN_SECRET: str

    """Postgres"""
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    @computed_field
    @property
    def postgres_dsn(self) -> PostgresDsn:
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            host=self.POSTGRES_SERVER,
            port=self.POSTGRES_PORT,
            path=self.POSTGRES_DB,
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
        )

    """Redis"""
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0
    REDIS_PASSWORD: str


settings = Settings()  # type: ignore
