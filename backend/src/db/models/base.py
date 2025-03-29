from typing import Annotated

from sqlalchemy import Integer, Identity
from sqlalchemy.orm import DeclarativeBase, mapped_column


class Base(DeclarativeBase):
    pass


# mapped types
int_pk = Annotated[
    int,
    mapped_column(
        Integer, Identity(always=True, start=1, increment=1), primary_key=True
    ),
]
