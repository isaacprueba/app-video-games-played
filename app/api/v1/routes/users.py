from fastapi import APIRouter, Depends, HTTPException, Query, status

from app.api.dependencies import get_catalog_service, get_user_service
from app.api.v1.schemas.catalog import GameSummaryResponse
from app.api.v1.schemas.common import PageMeta
from app.api.v1.schemas.users import UserLibraryItemResponse, UserLibraryResponse, UserProfileResponse
from app.application.services.catalog_service import CatalogService
from app.application.services.user_service import UserService
from app.core.config import settings
from app.domain.users.entities import UserLibraryItem, UserProfile

router = APIRouter()


def _profile_response(profile: UserProfile) -> UserProfileResponse:
    return UserProfileResponse(
        id=profile.id,
        display_name=profile.display_name,
        region=profile.region,
        favorite_genres=profile.favorite_genres,
        preferred_platforms=profile.preferred_platforms,
    )


def _library_item_response(
    item: UserLibraryItem,
    catalog_service: CatalogService,
) -> UserLibraryItemResponse:
    detail = catalog_service.get_game_detail(item.game_id)
    game_summary = GameSummaryResponse(
        id=detail.id if detail else item.game_id,
        title=detail.title if detail else "Unknown",
        platforms=[] if not detail else [
            {"id": platform.id, "name": platform.name, "family": platform.family}
            for platform in detail.platforms
        ],
        genres=[] if not detail else detail.genres,
        release_year=None if not detail else detail.release_year,
        publisher=None if not detail else detail.publisher,
    )
    return UserLibraryItemResponse(
        game=game_summary,
        status=item.status,
        last_played_at=item.last_played_at,
        hours_played=item.hours_played,
    )


@router.get("/{user_id}/profile", response_model=UserProfileResponse)
def get_user_profile(
    user_id: str,
    service: UserService = Depends(get_user_service),
) -> UserProfileResponse:
    profile = service.get_profile(user_id)
    if not profile:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")
    return _profile_response(profile)


@router.get("/{user_id}/library", response_model=UserLibraryResponse)
def get_user_library(
    user_id: str,
    page: int = Query(1, ge=1),
    page_size: int = Query(settings.default_page_size, ge=1),
    service: UserService = Depends(get_user_service),
    catalog_service: CatalogService = Depends(get_catalog_service),
) -> UserLibraryResponse:
    result = service.get_library(user_id, page=page, page_size=page_size)
    return UserLibraryResponse(
        items=[_library_item_response(item, catalog_service) for item in result.items],
        meta=PageMeta(
            page=result.page,
            page_size=result.page_size,
            total=result.total,
            total_pages=result.total_pages,
        ),
    )
