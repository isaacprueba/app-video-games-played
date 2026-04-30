from datetime import datetime, timezone

from fastapi import APIRouter

from app.schemas import GameSummary, Platform, UserLibraryItem, UserProfile

router = APIRouter()

_PLATFORM_PC = Platform(id="pc", name="PC")
_SAMPLE_GAME = GameSummary(
    id="game-001",
    title="Nebula Drift",
    platforms=[_PLATFORM_PC],
    genres=["Sci-Fi", "Roguelike"],
    release_year=2025,
)


@router.get("/{user_id}/profile", response_model=UserProfile)
def get_user_profile(user_id: str) -> UserProfile:
    return UserProfile(
        id=user_id,
        display_name="Player One",
        region="LATAM",
        favorite_genres=["RPG", "Aventura"],
        preferred_platforms=["pc", "ps5"],
    )


@router.get("/{user_id}/library", response_model=list[UserLibraryItem])
def get_user_library(user_id: str) -> list[UserLibraryItem]:
    return [
        UserLibraryItem(
            game=_SAMPLE_GAME,
            status="playing",
            last_played_at=datetime.now(timezone.utc),
            hours_played=12.5,
        )
    ]
