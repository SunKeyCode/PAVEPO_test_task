from fastapi import APIRouter

from api.dependencies import UserRepo
from schemas.users import CreateUserSchema

router = APIRouter(prefix="/users", tags=["Пользователи"])


@router.post("/")
async def crate_user(repo: UserRepo, user_data: CreateUserSchema):
    # just for debug
    created_user = await repo.create(user_data)
    return created_user


@router.get("/")
async def get_users(repo: UserRepo):
    return await repo.get_list()


@router.delete("/{user_id}")
async def delete_user(user_id: int, repo: UserRepo):
    pass


@router.patch("/user_id")
async def update_user_info(user_id: int, repo: UserRepo):
    pass
