from app.application.ports.catalog_repository import CatalogRepository
from app.data.sample_data import GAME_DETAILS, GAMES
from app.domain.catalog.entities import Game, GameDetail
from app.domain.catalog.filters import GameSearchFilters


class InMemoryCatalogRepository(CatalogRepository):
    def __init__(self) -> None:
        self._games = list(GAMES)
        self._details = dict(GAME_DETAILS)

    def search_games(self, filters: GameSearchFilters) -> list[Game]:
        query = filters.query.lower().strip()
        results = [game for game in self._games if query in game.title.lower()]
        if filters.platform:
            results = [
                game
                for game in results
                if any(platform.id == filters.platform for platform in game.platforms)
            ]
        if filters.genre:
            results = [game for game in results if filters.genre.lower() in (g.lower() for g in game.genres)]
        return results

    def get_game_detail(self, game_id: str) -> GameDetail | None:
        return self._details.get(game_id)
