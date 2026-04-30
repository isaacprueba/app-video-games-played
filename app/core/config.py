from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    app_name: str = os.getenv("APP_NAME", "Game Atlas API")
    environment: str = os.getenv("ENVIRONMENT", "local")
    version: str = os.getenv("APP_VERSION", "0.1.0")


settings = Settings()
