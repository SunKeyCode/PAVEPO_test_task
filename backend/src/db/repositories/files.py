from db.repositories.base import BaseRepository


class FileStorageRepository(BaseRepository):
    async def create(self):
        pass

    async def get(self, file_id: int):
        pass

    async def get_by_user(self, user_id: int):
        pass

    async def delete(self, file_id: int):
        pass
