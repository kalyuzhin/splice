from typing import Optional
from pydantic import EmailStr
from sqlmodel import SQLModel, Field


class BaseUser(SQLModel):
    username: str = Field(min_length=3, max_length=30)
    email: EmailStr
    first_name: str = Field(min_length=1, max_length=30)
    last_name: str = Field(min_length=1, max_length=30)


