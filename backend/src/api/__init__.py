from fastapi import APIRouter
from api.users import router as users_router
from api.files import router as files_router
from api.auth import router as auth_router
from constants import MAIN_PREFIX

main_router = APIRouter(prefix=MAIN_PREFIX)

main_router.include_router(users_router)
main_router.include_router(files_router)
main_router.include_router(auth_router)
