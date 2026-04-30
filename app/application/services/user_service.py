from app.application.ports.user_repository import UserRepository
from app.core.config import settings
from app.core.pagination import PageResult, paginate
from app.domain.users.entities import UserLibraryItem, UserProfile
from app.infrastructure.cache.base import Cache


class UserService:
    def __init__(self, repository: UserRepository, cache: Cache) -> None:
        self._repository = repository
        self._cache = cache

    def get_profile(self, user_id: str) -> UserProfile | None:
        cache_key = f"user:profile:{user_id}"
        cached = self._cache.get(cache_key)
        if cached:
            return cached
        profile = self._repository.get_profile(user_id)
        if profile:
            self._cache.set(cache_key, profile, settings.cache_ttl_seconds)
        return profile

    def get_library(self, user_id: str, page: int, page_size: int) -> PageResult[UserLibraryItem]:
        library = self._repository.get_library(user_id)
        return paginate(library, page, min(page_size, settings.max_page_size))
