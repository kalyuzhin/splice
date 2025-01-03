from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from app.models import UserPublic, CreateUser
from app.api.dependencies import SessionDep
from app import crud

router = APIRouter(prefix='/users', tags=['users'])


@router.post('/', response_model=UserPublic)
async def create_user(user_create: CreateUser, session: SessionDep):
    created_user = await crud.create_user(session, user_create)
    return created_user
    # return created_user
