from app.application.ports.content_repository import ContentRepository
from app.domain.content.entities import Entity, EventItem, Guide, NewsItem


class ContentService:
    def __init__(self, repository: ContentRepository) -> None:
        self._repository = repository

    def list_news(self) -> list[NewsItem]:
        return self._repository.list_news()

    def list_events(self, game_id: str | None = None) -> list[EventItem]:
        return self._repository.list_events(game_id)

    def list_guides(self, game_id: str | None = None) -> list[Guide]:
        return self._repository.list_guides(game_id)

    def list_entities(self, game_id: str | None = None) -> list[Entity]:
        return self._repository.list_entities(game_id)
