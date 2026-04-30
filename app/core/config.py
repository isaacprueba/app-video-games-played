from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    app_name: str = os.getenv("APP_NAME", "Game Atlas API")
    environment: str = os.getenv("ENVIRONMENT", "local")
    version: str = os.getenv("APP_VERSION", "0.2.0")
    api_prefix: str = os.getenv("API_PREFIX", "/api/v1")
    rate_limit_per_minute: int = int(os.getenv("RATE_LIMIT_PER_MINUTE", "120"))
    enable_rate_limit: bool = os.getenv("ENABLE_RATE_LIMIT", "true").lower() == "true"
    api_key: str | None = os.getenv("API_KEY")
    cache_ttl_seconds: int = int(os.getenv("CACHE_TTL_SECONDS", "60"))
    default_page_size: int = int(os.getenv("DEFAULT_PAGE_SIZE", "25"))
    max_page_size: int = int(os.getenv("MAX_PAGE_SIZE", "100"))


settings = Settings()
