import asyncio

from httpx import AsyncClient

from schemas.yandex_id import YandexIdInputSchema


def get_yandex_id_access_token():
    return "y0__xDJjs5hGOq_NiCZ38TVEhZ0o_mNE7fEULg7Revrui_VuQdI"


async def request_user_data_from_yandex_id() -> YandexIdInputSchema:
    async with AsyncClient() as client:
        params = {
            "oauth_token": get_yandex_id_access_token(),
            "format": "json",
        }
        url = "https://login.yandex.ru/info"
        response = await client.get(url, params=params)

        resp_as_dict = response.json()
        return YandexIdInputSchema(**resp_as_dict)
