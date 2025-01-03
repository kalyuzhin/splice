import uuid

from sqlmodel import Session, select
from .models import CreateUser, User
from .core.security import get_password_hash


async def create_user(session: Session, user_create: CreateUser) -> User:
    db_obj = User.model_validate(user_create, update={"password_hash": get_password_hash(user_create.password)})
    session.add(db_obj)
    await session.commit()
    await session.refresh(db_obj)
    return db_obj
