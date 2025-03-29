from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from db.models import Base
from db.models.base import int_pk


class FileModel(Base):
    __tablename__ = "file_storage"

    id: Mapped[int_pk]
    user_filename: Mapped[str] = mapped_column(String)
    system_filename: Mapped[str] = mapped_column(String)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", name="file_storage_user_id_fk"), nullable=False
    )

    user = relationship("User")
