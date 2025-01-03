from sqlmodel import SQLModel
from .config import settings
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base

engine = create_async_engine(str(settings.sqlalchemy_database_url), echo=True)
async_session = AsyncSession(bind=engine, expire_on_commit=False)
Base = declarative_base()


async def get_session() -> AsyncSession:
    async with async_session as session:
        yield session
