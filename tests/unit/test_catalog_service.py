from app.application.services.catalog_service import CatalogService
from app.domain.catalog.filters import GameSearchFilters
from app.infrastructure.cache.memory import InMemoryCache
from app.infrastructure.repositories.in_memory_catalog import InMemoryCatalogRepository


def test_search_games_filters_by_query() -> None:
    service = CatalogService(InMemoryCatalogRepository(), InMemoryCache())
    result = service.search_games(GameSearchFilters(query="Nebula"), page=1, page_size=10)
    assert result.total >= 1
    assert any(game.title == "Nebula Drift" for game in result.items)


def test_get_game_detail_returns_none_when_missing() -> None:
    service = CatalogService(InMemoryCatalogRepository(), InMemoryCache())
    assert service.get_game_detail("missing-game") is None
