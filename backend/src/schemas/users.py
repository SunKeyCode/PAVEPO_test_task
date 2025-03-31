from pydantic import BaseModel


class CreateUserSchema(BaseModel):
    login: str
    email: str
    name: str | None = None


class UpdateUserSchema(BaseModel):
    email: str | None = None
    name: str | None = None


class ResponseUserSchema(CreateUserSchema):
    id: int
