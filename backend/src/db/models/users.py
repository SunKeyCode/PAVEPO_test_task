from sqlalchemy import Identity, Boolean, Integer, String, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from db.models.base import Base


class YandexAccount(Base):
    __tablename__ = "yandex_account_table"
    id: Mapped[int] = mapped_column(Integer, Identity(always=False), primary_key=True)
    login: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    default_email: Mapped[str] = mapped_column(String)


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(
        Integer, Identity(always=True, start=1, increment=1), primary_key=True
    )
    login: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String)
    name: Mapped[str] = mapped_column(String, nullable=True)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False)
    yandex_id: Mapped[int] = mapped_column(
        ForeignKey("yandex_account_table.id", ondelete="CASCADE"),
        nullable=True,
        name="fk_user_yandex_account_table_id",
    )

    yandex_account = relationship(YandexAccount)
