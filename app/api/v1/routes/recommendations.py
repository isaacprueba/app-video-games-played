from fastapi import APIRouter, Depends

from app.api.dependencies import get_catalog_service, get_recommendation_service
from app.api.v1.schemas.catalog import GameSummaryResponse
from app.api.v1.schemas.recommendations import RecommendationResponse
from app.application.services.catalog_service import CatalogService
from app.application.services.recommendation_service import RecommendationService
from app.domain.recommendations.entities import RecommendationItem

router = APIRouter()


def _recommendation_response(
    recommendation: RecommendationItem,
    catalog_service: CatalogService,
) -> RecommendationResponse:
    detail = catalog_service.get_game_detail(recommendation.game_id)
    game_summary = GameSummaryResponse(
        id=detail.id if detail else recommendation.game_id,
        title=detail.title if detail else "Unknown",
        platforms=[] if not detail else [
            {"id": platform.id, "name": platform.name, "family": platform.family}
            for platform in detail.platforms
        ],
        genres=[] if not detail else detail.genres,
        release_year=None if not detail else detail.release_year,
        publisher=None if not detail else detail.publisher,
    )
    return RecommendationResponse(
        game=game_summary,
        reason=recommendation.reason,
        confidence=recommendation.confidence,
    )


@router.get("/{user_id}", response_model=list[RecommendationResponse])
def get_recommendations(
    user_id: str,
    service: RecommendationService = Depends(get_recommendation_service),
    catalog_service: CatalogService = Depends(get_catalog_service),
) -> list[RecommendationResponse]:
    recommendations = service.get_recommendations(user_id)
    return [
        _recommendation_response(recommendation, catalog_service)
        for recommendation in recommendations
    ]
