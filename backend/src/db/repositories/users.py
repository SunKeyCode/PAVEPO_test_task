from sqlalchemy import select, update

from db.models import User
from db.repositories.base import BaseRepository
from schemas.users import CreateUserSchema


class UserRepository(BaseRepository):
    async def create(self, user_data: CreateUserSchema) -> User:
        new_user = User(**user_data.dict())
        self.session.add(new_user)
        await self.session.commit()
        return new_user

    async def get(self, user_id: int) -> User:
        stmt = select(User).where(User.id == user_id)
        return self.session.scalar(stmt)

    async def get_list(self):
        scalar_result = await self.session.scalars(select(User))
        return scalar_result.all()

    async def update(self, user_id: int, **values) -> User:
        stmt = update(User).where(User.id == user_id).values(values).returning(User)
        return await self.session.scalar(stmt)
