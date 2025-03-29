from sqlalchemy import select, update

from db.models import User
from db.repositories.base import BaseRepository
from schemas.users import InputUserSchema


class UserRepository(BaseRepository):
    async def create(self, user_data: InputUserSchema) -> User:
        new_user = User(**user_data.dict())
        self.session.add(new_user)
        await self.session.commit()
        return new_user

    async def get(self, user_id: int) -> User:
        stmt = select(User).where(User.id == user_id)
        return self.session.scalar(stmt)

    async def update(self, user_id: int, **values) -> User:
        stmt = update(User).where(User.id == user_id).values(values).returning(User)
        return await self.session.scalar(stmt)
