import asyncio

from bootstrap.users import create_superuser
from db.session import get_session
from exceptions import UserAlreadyExists


async def main():
    async with get_session() as session:
        try:
            await create_superuser(session=session)
        except UserAlreadyExists as exc:
            # TODO вывести лог в консоль
            pass


if __name__ == "__main__":
    asyncio.run(main())
