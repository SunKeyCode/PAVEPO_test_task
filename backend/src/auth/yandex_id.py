from fastapi.exceptions import HTTPException

from httpx import AsyncClient
from starlette import status

from schemas.yandex_id import YandexIdInputSchema, YandexIdToken
from settings.config import get_settings


async def get_yandex_id_access_token_with_auth_code(auth_code: str) -> YandexIdToken:
    """
    Получить токен аутентификации Yandex ID по коду подтверждения, полученному из
    https://oauth.yandex.ru/authorize?response_type=code&client_id=<client_id>

    :param auth_code: код подтверждения
    :return: объект токена
    """
    settings = get_settings()
    url = "https://oauth.yandex.ru/token"
    boby = {
        "grant_type": "authorization_code",
        "code": auth_code,
        "client_id": settings.CLIENT_ID,
        "client_secret": settings.CLIENT_SECRET,
    }
    async with AsyncClient() as client:
        response = await client.post(url, data=boby)
        if response.status_code == 200:
            return YandexIdToken(**response.json())
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=response.text)


async def request_user_data_from_yandex_id_by_token(token: str) -> YandexIdInputSchema:
    """
    Запросить данные пользователя аккаунта Yandex по токену аутентификации.

    :param token: токен аутентификации
    :return: данные пользователя в виде схемы YandexIdInputSchema
    """
    url = "https://login.yandex.ru/info"
    params = {
        "oauth_token": token,
        "format": "json",
    }
    async with AsyncClient() as client:
        response = await client.get(url, params=params)

        resp_as_dict = response.json()
        return YandexIdInputSchema(**resp_as_dict)


async def request_yandex_account_data(code: str) -> YandexIdInputSchema:
    """
    Запрашивает данные аккаунта Yandex по коду подтверждения.

    :param code: код подтверждения
    :return:
    """

    token = await get_yandex_id_access_token_with_auth_code(auth_code=code)
    user_data = await request_user_data_from_yandex_id_by_token(
        token=token.access_token
    )
    return user_data
