from pydantic import BaseModel


class CreateUserSchema(BaseModel):
    login: str
    email: str
    is_superuser: bool = False


class UpdateUserSchema(BaseModel):
    pass
