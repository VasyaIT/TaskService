from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    TITLE_APP: str = Field(default="Task Service")
    CORS_ALLOWED_ORIGINS: str
    DEBUG: bool

    @property
    def cors_allowed_origins(self) -> list[str]:
        return self.CORS_ALLOWED_ORIGINS.split()

    @property
    def docs_url(self) -> str:
        return "/docs" if self.DEBUG else ""

    @property
    def openapi_url(self) -> str:
        return "/openapi.json" if self.DEBUG else ""


settings = Settings()
