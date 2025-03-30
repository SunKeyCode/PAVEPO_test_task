import asyncio

from sqlalchemy import select, update, delete

from db.models import User, Password
from db.repositories.base import BaseRepository
from db.session import get_session
from schemas.users import CreateUserSchema
from utils import hash_password


class UserRepository(BaseRepository):
    async def create(
        self, user_data: CreateUserSchema, password: str | None = None
    ) -> User:
        new_user = User(**user_data.dict())
        self.session.add(new_user)
        await self.session.flush()
        if password is not None:
            password_model = Password(
                user_id=new_user.id, password=hash_password(password)
            )
            self.session.add(password_model)
        await self.session.commit()
        return new_user

    async def get(self, user_id: int) -> User:
        stmt = select(User).where(User.id == user_id)
        return await self.session.scalar(stmt)

    async def get_list(self):
        scalar_result = await self.session.scalars(select(User))
        return scalar_result.all()

    async def update(self, user_id: int, **values) -> User:
        stmt = update(User).where(User.id == user_id).values(values).returning(User)
        return await self.session.scalar(stmt)

    async def get_by_login(self, login: str):
        stmt = select(User).where(User.login == login)
        return await self.session.scalar(stmt)

    async def get_by_yandex_id(self, yandex_id: int):
        stmt = select(User).where(User.yandex_id == yandex_id)
        return await self.session.scalar(stmt)

    async def delete(self, user_id: int):
        return await self.session.execute(
            delete(User).where(User.id == user_id).returning(User.id)
        )


async def get_user():
    async with get_session() as session:
        repo = UserRepository(session)
        user = await repo.get_by_login("some_login")
    return user


if __name__ == "__main__":
    user = asyncio.run(get_user())
