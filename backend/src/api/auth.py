from fastapi import APIRouter, Depends

from auth.deps import get_auth_user
from auth.jwt import encode_token
from auth.yandex_id import request_user_data_from_yandex_id
from db.repositories.users import UserRepository
from db.repositories.yandex_account import YandexAccountRepository
from db.session import get_session
from schemas.users import CreateUserSchema

router = APIRouter(prefix="/auth", tags=["Аутентификация"])


@router.get("/yandex_auth")
async def get_yandex_auth_data():
    account_schema = await request_user_data_from_yandex_id()
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

        token = encode_token(user_id=str(user.id))

        return token


@router.get("/create_token/{user_id}")
async def get_token(user_id: int):
    return encode_token(str(user_id))


@router.get("/refresh_token")
async def refresh_token(user=Depends(get_auth_user)):
    return user
