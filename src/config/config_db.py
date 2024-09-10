from pydantic import Field
from pydantic_settings import BaseSettings


class DataBaseConfig(BaseSettings):
    DB_NAME: str = Field(default="DB.db")

    @property
    def database_url(self) -> str:
        return f"sqlite+aiosqlite:///{self.DB_NAME}"


config_db = DataBaseConfig()
