import asyncio
from fastapi.exceptions import HTTPException

from httpx import AsyncClient
from starlette import status

from schemas.yandex_id import YandexIdInputSchema, YandexIdToken
from settings.config import get_settings


def get_yandex_id_access_token():
    return "y0__xDJjs5hGOq_NiCZ38TVEhZ0o_mNE7fEULg7Revrui_VuQdI"


async def get_yandex_id_access_token_with_auth_code(auth_code: str) -> YandexIdToken:
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
    token = await get_yandex_id_access_token_with_auth_code(auth_code=code)
    user_data = await request_user_data_from_yandex_id_by_token(
        token=token.access_token
    )
    return user_data
