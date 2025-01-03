from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal
from pydantic import PostgresDsn
from pydantic_core import MultiHostUrl


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_ignore_empty=True,
        extra='ignore',
    )

    API_V1_STR: str = "/api/v1"

    PROJECT_NAME: str = 'Test'

    ENVIRONMENT: Literal['production', 'development'] = 'development'

    POSTGRES_HOST: str = 'localhost'
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = 'postgres'
    POSTGRES_PASSWORD: str = ''
    POSTGRES_DB: str = 'postgres'

    FRONTEND_HOST: str = 'http://localhost:5173'

    @property
    def sqlalchemy_database_url(self) -> str:
        # return MultiHostUrl.build(
        #     scheme='postgres+asyncpg',
        #     username=self.POSTGRES_USER,
        #     password=self.POSTGRES_PASSWORD,
        #     host=self.POSTGRES_HOST,
        #     port=self.POSTGRES_PORT,
        #     path=self.POSTGRES_DB,
        # )
        return f"postgresql+asyncpg://{self.POSTGRES_USER}{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"


settings = Settings()
