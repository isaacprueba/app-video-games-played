from app.application.ports.catalog_repository import CatalogRepository
from app.core.config import settings
from app.core.pagination import PageResult, paginate
from app.domain.catalog.entities import Game, GameDetail
from app.domain.catalog.filters import GameSearchFilters
from app.infrastructure.cache.base import Cache


class CatalogService:
    def __init__(self, repository: CatalogRepository, cache: Cache) -> None:
        self._repository = repository
        self._cache = cache

    def search_games(
        self,
        filters: GameSearchFilters,
        page: int,
        page_size: int,
    ) -> PageResult[Game]:
        cache_key = f"catalog:search:{filters.query}:{filters.platform}:{filters.genre}:{page}:{page_size}"
        cached = self._cache.get(cache_key)
        if cached:
            return cached
        results = self._repository.search_games(filters)
        paged = paginate(results, page, min(page_size, settings.max_page_size))
        self._cache.set(cache_key, paged, settings.cache_ttl_seconds)
        return paged

    def get_game_detail(self, game_id: str) -> GameDetail | None:
        cache_key = f"catalog:detail:{game_id}"
        cached = self._cache.get(cache_key)
        if cached:
            return cached
        detail = self._repository.get_game_detail(game_id)
        if detail:
            self._cache.set(cache_key, detail, settings.cache_ttl_seconds)
        return detail
