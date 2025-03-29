from pydantic import BaseModel


class InputUserSchema(BaseModel):
    login: str
    email: str
    is_superuser: bool = False
