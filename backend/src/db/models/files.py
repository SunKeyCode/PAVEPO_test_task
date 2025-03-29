from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from db.models import Base
from db.models.base import int_pk


class File(Base):
    __tablename__ = "file_storage"

    id: Mapped[int_pk]
    user_name: Mapped[str] = mapped_column(String)
    system_name: Mapped[str] = mapped_column(String)
