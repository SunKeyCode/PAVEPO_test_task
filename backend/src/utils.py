import pathlib
import uuid
import aiofiles
from passlib.context import CryptContext

from constants import FILES_DIR


async def save_file_to_filesystem(file_obj: bytes, system_filename: str):
    if not pathlib.Path(FILES_DIR).exists():
        pathlib.Path(FILES_DIR).mkdir()
    async with aiofiles.open(FILES_DIR / system_filename, "wb") as file:
        await file.write(file_obj)
        await file.flush()


def generate_system_filename():
    return str(uuid.uuid4())


def hash_password(password: str):
    hasher = CryptContext(schemes=["sha256_crypt"])
    return hasher.hash(password)


def verify_password(hashed: str, password: str) -> str:
    hasher = CryptContext(schemes=["sha256_crypt"])
    return hasher.verify(password, hashed)
