from fastapi import APIRouter

from auth.yandex_id import request_user_data
from db.repositories.users import UserRepository
from db.repositories.yandex_account import YandexAccountRepository
from db.session import get_session
from schemas.users import CreateUserSchema

router = APIRouter(prefix="/auth", tags=["Аутентификация"])


@router.get("/yandex_auth")
async def get_yandex_auth_data():
    account_schema = await request_user_data()
    async with get_session() as session:
        repo = YandexAccountRepository(session)
        account = await repo.get_or_create(account_schema)
        user_repo = UserRepository(session)
        user = await user_repo.get_by_yandex_id(yandex_id=account.id)
        if user is None:
            user_schema = CreateUserSchema(
                login=account.login, email=account.default_email
            )
            user = await user_repo.create(user_schema)
            user.yandex_id = account.id
            await session.commit()

        return user
