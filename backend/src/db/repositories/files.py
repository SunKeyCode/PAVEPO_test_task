from sqlalchemy import select

from db.models import FileModel
from db.repositories.base import BaseRepository
from schemas.files import CreateFileSchema


class FileStorageRepository(BaseRepository):
    async def create(self, file_info: CreateFileSchema, user_id: int) -> FileModel:
        new_file = FileModel(
            user_filename=file_info.user_filename,
            system_filename=file_info.system_filename,
            user_id=user_id,
        )
        self.session.add(new_file)
        await self.session.commit()
        return new_file

    async def get(self, file_id: int) -> FileModel:
        file_scalar_result = await self.session.scalar(
            select(FileModel).where(FileModel.id == file_id)
        )
        return file_scalar_result

    async def get_by_user(self, user_id: int) -> list[FileModel]:
        files_scalar_result = await self.session.scalars(
            select(FileModel).where(FileModel.user_id == user_id)
        )
        return files_scalar_result.all()

    async def delete(self, file_id: int):
        pass
