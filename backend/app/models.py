import uuid

from typing import Optional
from pydantic import EmailStr
from sqlmodel import SQLModel, Field


class BaseUser(SQLModel):
    username: str = Field(min_length=3, max_length=30)
    email: EmailStr = Field(unique=True, index=True, max_length=255)
    first_name: str | None = Field(default=None, min_length=1, max_length=30)
    last_name: str | None = Field(default=None, min_length=1, max_length=30)


class CreateUser(BaseUser):
    password: str = Field(min_length=8, max_length=40)


class UserPublic(BaseUser):
    id: uuid.UUID


class User(BaseUser, table=True):
    __tablename__ = "users"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    password_hash: str
