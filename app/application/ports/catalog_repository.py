from typing import Protocol

from app.domain.catalog.entities import Game, GameDetail
from app.domain.catalog.filters import GameSearchFilters


class CatalogRepository(Protocol):
    def search_games(self, filters: GameSearchFilters) -> list[Game]:
        raise NotImplementedError

    def get_game_detail(self, game_id: str) -> GameDetail | None:
        raise NotImplementedError
