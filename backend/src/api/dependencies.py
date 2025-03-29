from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.repositories.files import FileStorageRepository
from db.repositories.users import UserRepository
from db.session import get_session


async def get_async_session():
    async with get_session() as session:
        yield session


SessionDep = Annotated[AsyncSession, Depends(get_async_session)]


def get_user_repository(session: SessionDep):
    return UserRepository(session=session)


def get_file_repository(session: SessionDep):
    return FileStorageRepository(session=session)


UserRepo = Annotated[UserRepository, Depends(get_user_repository)]

FileRepo = Annotated[FileStorageRepository, Depends(get_file_repository)]
