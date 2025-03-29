from fastapi import APIRouter

from api.dependencies import UserRepo
from schemas.users import InputUserSchema

router = APIRouter(prefix="/users", tags=["Пользователи"])


@router.get("/")
async def get_users():
    return "OK"


@router.post("/")
async def crate_user(repo: UserRepo, user_data: InputUserSchema):
    # just for debug
    await repo.create(user_data)
