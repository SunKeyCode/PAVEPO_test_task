from pydantic import BaseModel


class YandexIdInputSchema(BaseModel):
    id: int
    login: str
    default_email: str
    # phone: str
