from app.application.ports.user_repository import UserRepository
from app.data.sample_data import USER_LIBRARY, USER_PROFILES
from app.domain.users.entities import UserLibraryItem, UserProfile


class InMemoryUserRepository(UserRepository):
    def __init__(self) -> None:
        self._profiles = dict(USER_PROFILES)
        self._library = {user_id: list(items) for user_id, items in USER_LIBRARY.items()}

    def get_profile(self, user_id: str) -> UserProfile | None:
        return self._profiles.get(user_id)

    def get_library(self, user_id: str) -> list[UserLibraryItem]:
        return list(self._library.get(user_id, []))
