from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    app_name: str = "Agent API"
    admin_email: str
    database_url: str

settings = Settings()
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Agent API"
    admin_email: str
    database_url: str

    class Config:
        env_file = ".env"

settings = Settings()