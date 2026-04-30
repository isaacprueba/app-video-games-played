from typing import Protocol

from app.domain.users.entities import UserLibraryItem, UserProfile


class UserRepository(Protocol):
    def get_profile(self, user_id: str) -> UserProfile | None:
        ...

    def get_library(self, user_id: str) -> list[UserLibraryItem]:
        ...
