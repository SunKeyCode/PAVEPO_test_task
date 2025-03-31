from fastapi import APIRouter, UploadFile, Depends
from starlette.responses import FileResponse

from api.dependencies import FileRepo
from auth.deps import UserDep
from constants import FILES_DIR
from schemas.files import CreateFileSchema, ResponseFileSchema
from utils import save_file_to_filesystem

router = APIRouter(prefix="/files", tags=["Работа с файлами"])


@router.get("/download/{file_id}")
async def download_file(
    _: UserDep,
    file_id: int,
    repo: FileRepo,
):
    """Скачать ранее загруженный файл"""

    file_info = await repo.get(file_id=file_id)
    return FileResponse(
        path=FILES_DIR / file_info.system_filename,
        filename=file_info.user_filename,
        media_type="application/octet-stream",
    )


@router.post("/upload")
async def upload_file(
    user: UserDep,
    file: UploadFile,
    repo: FileRepo,
    file_info: CreateFileSchema = Depends(),
) -> int:
    """
    Загрузить файл.

    **filename** - пользовательское имя файла.
    """

    await save_file_to_filesystem(
        file_obj=await file.read(), system_filename=file_info.system_filename
    )
    new_file = await repo.create(file_info=file_info, user_id=user.id)

    return new_file.id


@router.get("/")
async def get_files_by_user_id(
    user: UserDep,
    repo: FileRepo,
) -> list[ResponseFileSchema]:
    """Список файлов пользователя."""
    files = await repo.get_by_user(user_id=user.id)
    return files
