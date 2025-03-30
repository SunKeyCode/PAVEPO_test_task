from fastapi import APIRouter, status

from api.dependencies import UserRepo
from auth.deps import UserDep, SuperuserDep
from schemas.users import UpdateUserSchema

router = APIRouter(prefix="/users", tags=["Пользователи"])


@router.get("/me")
async def get_user(user: UserDep):
    return user


@router.get("/")
async def get_users(_: SuperuserDep, repo: UserRepo):
    return await repo.get_list()


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(_: SuperuserDep, user_id: int, repo: UserRepo):
    await repo.delete(user_id=user_id)


@router.patch("/")
async def update_user_info(
    user: UserDep,
    repo: UserRepo,
    user_data: UpdateUserSchema,
):
    user_dict = user_data.dict(exclude_none=True)
    user = await repo.update(user_id=user.id, **user_dict)
    return user
