from typing import Protocol

from app.domain.content.entities import Entity, EventItem, Guide, NewsItem


class ContentRepository(Protocol):
    def list_news(self) -> list[NewsItem]:
        raise NotImplementedError

    def list_events(self, game_id: str | None = None) -> list[EventItem]:
        raise NotImplementedError

    def list_guides(self, game_id: str | None = None) -> list[Guide]:
        raise NotImplementedError

    def list_entities(self, game_id: str | None = None) -> list[Entity]:
        raise NotImplementedError
