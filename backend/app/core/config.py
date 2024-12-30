from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal
from pydantic import PostgresDsn


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='../../.env',
        env_ignore_empty=True,
        extra='ignore',
    )

    PROJECT_NAME: str

    ENVIRONMENT: Literal['production', 'development'] = 'development'

    POSTGRES_HOST: str = 'localhost'
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = 'postgres'
    POSTGRES_PASSWORD: str = ''
    POSTGRES_DB: str = 'postgres'

    FRONTEND_HOST: str = 'http://localhost:5173'

    @property
    def sqlalchemy_database_url(self) -> PostgresDsn:
        return PostgresDsn.build(
            scheme='postgres+asyncpg',
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_HOST,
            port=self.POSTGRES_PORT,
            path=self.POSTGRES_DB,
        )


settings = Settings()
