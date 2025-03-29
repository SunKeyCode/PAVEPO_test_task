from fastapi import APIRouter

router = APIRouter(prefix="/files", tags=["Работа с файлами"])


@router.get("/")
def download_file():
    pass
