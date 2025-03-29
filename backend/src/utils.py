import pathlib
import uuid
import aiofiles
from fastapi import UploadFile

from constants import FILES_DIR
from schemas.files import CreateFileSchema


async def save_file_to_filesystem(file_obj: bytes, system_filename: str):
    if not pathlib.Path(FILES_DIR).exists():
        pathlib.Path(FILES_DIR).mkdir()
    async with aiofiles.open(FILES_DIR / system_filename, "wb") as file:
        await file.write(file_obj)
        await file.flush()


def generate_system_filename():
    return str(uuid.uuid4())
