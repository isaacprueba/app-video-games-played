from fastapi import APIRouter

from app.schemas import GameSummary, Platform, RecommendationItem

router = APIRouter()

_SAMPLE_GAME = GameSummary(
    id="game-003",
    title="Skyforge Legends",
    platforms=[Platform(id="pc", name="PC")],
    genres=["Action", "MMO"],
    release_year=2026,
)


@router.get("/{user_id}", response_model=list[RecommendationItem])
def get_recommendations(user_id: str) -> list[RecommendationItem]:
    return [
        RecommendationItem(
            game=_SAMPLE_GAME,
            reason="Coincide con tu interés en cooperativo y fantasía épica.",
            confidence=0.82,
        )
    ]
