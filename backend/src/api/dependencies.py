from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.repositories.users import UserRepository
from db.session import get_session

SessionDep = Annotated[AsyncSession, Depends(get_session)]


def get_user_repository(session: SessionDep):
    return UserRepository(session=session)


UserRepo = Annotated[UserRepository, Depends(get_user_repository)]
