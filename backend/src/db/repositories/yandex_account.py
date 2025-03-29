from sqlalchemy import select

from db.models import YandexAccount
from db.repositories.base import BaseRepository
from schemas.yandex_id import YandexIdInputSchema


class YandexAccountRepository(BaseRepository):
    async def create(self, data: YandexIdInputSchema):
        account = YandexAccount(**data.dict())
        self.session.add(account)
        await self.session.commit()
        return account

    async def get(self, yandex_id: int):
        stmt = select(YandexAccount).where(YandexAccount.id == yandex_id)

        return await self.session.scalar(stmt)

    async def get_or_create(self, data: YandexIdInputSchema):
        account = await self.get(data.id)
        if account is None:
            account = await self.create(data=data)

        return account
