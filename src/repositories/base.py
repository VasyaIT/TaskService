from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepository:
    def __init__(self, async_session: AsyncSession) -> None:
        self.session = async_session
