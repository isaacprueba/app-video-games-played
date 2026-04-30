from fastapi import APIRouter, Depends, HTTPException, Query, status

from app.api.dependencies import get_catalog_service
from app.api.v1.mappers import to_game_detail_response, to_game_summary_response
from app.api.v1.schemas.catalog import GameDetailResponse, GameSearchResponse, GameSummaryResponse
from app.api.v1.schemas.common import PageMeta
from app.application.services.catalog_service import CatalogService
from app.core.config import settings
from app.domain.catalog.filters import GameSearchFilters

router = APIRouter()


@router.get("/search", response_model=GameSearchResponse)
def search_games(
    q: str = Query(..., min_length=2),
    platform: str | None = None,
    genre: str | None = None,
    region: str | None = None,
    page: int = Query(1, ge=1),
    page_size: int = Query(settings.default_page_size, ge=1),
    service: CatalogService = Depends(get_catalog_service),
) -> GameSearchResponse:
    filters = GameSearchFilters(query=q, platform=platform, genre=genre, region=region)
    result = service.search_games(filters, page=page, page_size=page_size)
    return GameSearchResponse(
        items=[to_game_summary_response(game) for game in result.items],
        meta=PageMeta(
            page=result.page,
            page_size=result.page_size,
            total=result.total,
            total_pages=result.total_pages,
        ),
    )


@router.get("/{game_id}", response_model=GameDetailResponse)
def get_game(
    game_id: str,
    service: CatalogService = Depends(get_catalog_service),
) -> GameDetailResponse:
    detail = service.get_game_detail(game_id)
    if not detail:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Game not found.")
    return to_game_detail_response(detail)
