from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from sqlalchemy.ext.asyncio import async_sessionmaker

from settings.config import get_settings


def get_engine() -> AsyncEngine:
    engine = create_async_engine(
        url=get_settings().async_db_url.unicode_string(),
        pool_pre_ping=True,
        pool_size=20,
    )
    return engine


def async_session_maker() -> async_sessionmaker:
    return async_sessionmaker(
        bind=get_engine(),
        autoflush=False,
        autocommit=False,
        expire_on_commit=False,
    )


async def get_session():
    session_maker = async_session_maker()
    async with session_maker() as session:
        try:
            yield session
        except Exception as exc:
            await session.rollback()
            raise exc
        finally:
            await session.close()
