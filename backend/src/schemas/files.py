import uuid
from functools import cached_property

from pydantic import BaseModel, Field


class CreateFileSchema(BaseModel):
    user_filename: str = Field(alias="filename")

    @cached_property
    def system_filename(self):
        return str(uuid.uuid4())


class ResponseFileSchema(BaseModel):
    id: int
    filename: str
