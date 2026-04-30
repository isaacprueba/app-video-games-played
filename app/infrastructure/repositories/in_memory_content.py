from app.application.ports.content_repository import ContentRepository
from app.data.sample_data import ENTITIES, EVENTS, GUIDES, NEWS
from app.domain.content.entities import Entity, EventItem, Guide, NewsItem


class InMemoryContentRepository(ContentRepository):
    def __init__(self) -> None:
        self._news = list(NEWS)
        self._events = list(EVENTS)
        self._guides = list(GUIDES)
        self._entities = list(ENTITIES)

    def list_news(self) -> list[NewsItem]:
        return list(self._news)

    def list_events(self, game_id: str | None = None) -> list[EventItem]:
        if not game_id:
            return list(self._events)
        return [event for event in self._events if event.game_id == game_id]

    def list_guides(self, game_id: str | None = None) -> list[Guide]:
        if not game_id:
            return list(self._guides)
        return [guide for guide in self._guides if guide.game_id == game_id]

    def list_entities(self, game_id: str | None = None) -> list[Entity]:
        if not game_id:
            return list(self._entities)
        return [entity for entity in self._entities if entity.game_id == game_id]
