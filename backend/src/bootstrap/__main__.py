import asyncio

from bootstrap.users import create_superuser
from db.session import get_session
from exceptions import UserAlreadyExists
from loguru import logger


async def main():
    async with get_session() as session:
        try:
            await create_superuser(session=session)
        except UserAlreadyExists:
            logger.info("Суперпользователь уже существует.")


if __name__ == "__main__":
    asyncio.run(main())
