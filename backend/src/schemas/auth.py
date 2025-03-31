from pydantic import BaseModel


class AccessTokenSchema(BaseModel):
    token: str
    token_type: str = "bearer"


class UserCreds(BaseModel):
    login: str
    password: str
