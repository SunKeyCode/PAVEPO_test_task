from pydantic import BaseModel


class YandexIdInputSchema(BaseModel):
    id: int
    login: str
    # email: str
    # phone: str
