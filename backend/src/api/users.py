from fastapi import APIRouter

from api.dependencies import UserRepo
from auth.deps import UserDep
from schemas.users import CreateUserSchema

router = APIRouter(prefix="/users", tags=["Пользователи"])


@router.post("/")
async def crate_user(repo: UserRepo, user_data: CreateUserSchema):
    # just for debug
    created_user = await repo.create(user_data)
    return created_user


@router.get("/me")
async def get_user(user: UserDep):
    return user


@router.get("/")
async def get_users(repo: UserRepo):
    return await repo.get_list()


@router.delete("/{user_id}")
async def delete_user(user_id: int, repo: UserRepo):
    pass


@router.patch("/")
async def update_user_info(user: UserDep, repo: UserRepo):
    repo.update(user_id=user.id)
