from fastapi import APIRouter, Depends

from auth.deps import UserDep, get_access_token
from auth.jwt import encode_token, refresh_access_token
from auth.yandex_id import request_yandex_account_data
from db.repositories.users import UserRepository
from db.repositories.yandex_account import YandexAccountRepository
from db.session import get_session
from schemas.auth import AccessTokenSchema
from schemas.users import CreateUserSchema

router = APIRouter(prefix="/auth", tags=["Аутентификация"])


@router.get("/yandex_auth")
async def get_yandex_auth_data(code: str):
    """
    Авторизация через Яндекс ID, с помощью кода подтверждения.

    :param code: код подтверждения полученный пользователем
    :return:
    """
    account_schema = await request_yandex_account_data(code=code)
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

        return AccessTokenSchema(token=token)


@router.get("/refresh_token")
async def refresh_token(
    _: UserDep, token=Depends(get_access_token)
) -> AccessTokenSchema:
    return AccessTokenSchema(token=refresh_access_token(token))
