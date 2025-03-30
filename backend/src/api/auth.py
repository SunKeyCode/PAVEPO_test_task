from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from api.dependencies import SessionDep, UserRepo
from auth.deps import UserDep, get_access_token
from auth.jwt import encode_token, refresh_access_token
from auth.yandex_id import request_yandex_account_data
from db.repositories.users import UserRepository
from db.repositories.yandex_account import YandexAccountRepository
from schemas.auth import AccessTokenSchema, UserCreds
from schemas.users import CreateUserSchema
from utils import verify_password

router = APIRouter(prefix="/auth", tags=["Аутентификация"])


@router.get("/yandex_auth")
async def get_yandex_auth_data(code: str, session: SessionDep):
    """
    Авторизация через Яндекс ID, с помощью кода подтверждения.


    :param session: сессия для работы с БД
    :param code: код подтверждения полученный пользователем
    :return:
    """
    account_schema = await request_yandex_account_data(code=code)
    repo = YandexAccountRepository(session)
    account = await repo.get_or_create(account_schema)

    user_repo = UserRepository(session)
    user = await user_repo.get_by_yandex_id(yandex_id=account.id)
    if user is None:
        user_schema = CreateUserSchema(login=account.login, email=account.default_email)
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


@router.post("/login")
async def login(creds: UserCreds, repo: UserRepo) -> AccessTokenSchema:
    user = await repo.get_by_login(creds.login)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Пользователь не найден"
        )
    if not user.password or not verify_password(user.password.password, creds.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Неверный логин или пароль",
        )
    token = encode_token(user_id=str(user.id))

    return AccessTokenSchema(token=token)
