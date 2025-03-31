from pydantic import BaseModel


class YandexIdInputSchema(BaseModel):
    id: int
    login: str
    default_email: str


class YandexIdToken(BaseModel):
    token_type: str
    access_token: str
    expires_in: int
    refresh_token: str
