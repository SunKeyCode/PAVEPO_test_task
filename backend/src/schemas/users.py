from pydantic import BaseModel


class CreateUserSchema(BaseModel):
    login: str
    email: str
    name: str | None
    is_superuser: bool = False


class UpdateUserSchema(BaseModel):
    email: str | None = None
    name: str | None = None
