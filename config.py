<<<<<<< HEAD
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    app_name: str = "Agent API"
    admin_email: str
    database_url: str

settings = Settings()
=======
>>>>>>> a2600ba (update 30/12/2025- 4pm)
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Agent API"
    admin_email: str
    database_url: str

    class Config:
        env_file = ".env"

<<<<<<< HEAD
settings = Settings()
=======
settings = Settings()
>>>>>>> a2600ba (update 30/12/2025- 4pm)
