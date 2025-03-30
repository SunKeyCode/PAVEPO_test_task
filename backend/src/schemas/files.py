import uuid
from functools import cached_property

from pydantic import BaseModel, Field, field_validator

from constants import FILES_DIR


class CreateFileSchema(BaseModel):
    user_filename: str = Field(alias="filename")

    @cached_property
    def system_filename(self):
        return str(uuid.uuid4())


class ResponseFileSchema(BaseModel):
    id: int
    filename: str = Field(validation_alias="user_filename")
    path: str = Field(validation_alias="system_filename")

    @field_validator("path")
    @classmethod
    def validate_path(cls, value):
        return FILES_DIR / value
