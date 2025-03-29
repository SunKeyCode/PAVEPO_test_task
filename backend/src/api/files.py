from fastapi import APIRouter

router = APIRouter(prefix="/files", tags=["Работа с файлами"])


@router.get("/")
async def download_file():
    pass


@router.post("/")
async def upload_file():
    pass


@router.get("/list/{user_id}")
async def get_files_by_user_id(user_id: int):
    pass
