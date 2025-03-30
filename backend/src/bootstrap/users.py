from sqlalchemy.ext.asyncio import AsyncSession

from db.repositories.users import UserRepository
from exceptions import UserAlreadyExists
from schemas.users import CreateUserSchema
from settings.config import get_settings


async def create_superuser(session: AsyncSession):
    settings = get_settings()

    repo = UserRepository(session=session)

    user = await repo.get_by_login(settings.SUPERUSER_LOGIN)
    if user is not None:
        raise UserAlreadyExists("Суперпользователь уже существует")

    user = await repo.create(
        user_data=CreateUserSchema(
            login=get_settings().SUPERUSER_LOGIN,
            email=get_settings().SUPERUSER_EMAIL,
        ),
        password=settings.SUPERUSER_PASS,
        is_superuser=True,
    )

    return user
