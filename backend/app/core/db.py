from sqlmodel import SQLModel
from .config import settings
from sqlalchemy import Column, String, Integer, ForeignKey, text
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base

engine = create_async_engine(str(settings.sqlalchemy_database_url), echo=True)
async_session = AsyncSession(bind=engine, expire_on_commit=False)
Base = declarative_base()


async def get_session() -> AsyncSession:
    async with async_session as session:
        yield session


async def init_db():
    try:
        async with async_session as session:
            await session.execute(text('SELECT 1;'))
            print('Database is ready for use')
            return
    except Exception as e:
        print(e)
        raise e


import asyncio

# asyncio.run(init_db())
