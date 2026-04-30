from fastapi import APIRouter, Query

from app.schemas import GameDetail, GameSummary, Platform

router = APIRouter()

_PLATFORMS = {
    "pc": Platform(id="pc", name="PC"),
    "ps5": Platform(id="ps5", name="PlayStation 5"),
    "switch": Platform(id="switch", name="Nintendo Switch"),
}

_GAMES = [
    GameSummary(
        id="game-001",
        title="Nebula Drift",
        platforms=[_PLATFORMS["pc"], _PLATFORMS["ps5"]],
        genres=["Sci-Fi", "Roguelike"],
        release_year=2025,
    ),
    GameSummary(
        id="game-002",
        title="Mythic Grove",
        platforms=[_PLATFORMS["switch"]],
        genres=["Adventure", "Simulation"],
        release_year=2024,
    ),
]

_GAME_DETAILS = {
    "game-001": GameDetail(
        **_GAMES[0].model_dump(),
        description="Explora sectores dinámicos con naves modulares y eventos galácticos.",
        multiplayer_modes=["co-op", "ranked"],
        entities_count=42,
        guides_count=8,
    ),
    "game-002": GameDetail(
        **_GAMES[1].model_dump(),
        description="Gestiona un bosque místico con criaturas y misiones colaborativas.",
        multiplayer_modes=["local-coop"],
        entities_count=28,
        guides_count=5,
    ),
}


@router.get("/search", response_model=list[GameSummary])
def search_games(
    q: str = Query(..., min_length=2),
    platform: str | None = None,
) -> list[GameSummary]:
    query = q.lower().strip()
    results = [game for game in _GAMES if query in game.title.lower()]
    if platform:
        results = [game for game in results if any(p.id == platform for p in game.platforms)]
    return results


@router.get("/{game_id}", response_model=GameDetail)
def get_game(game_id: str) -> GameDetail:
    return _GAME_DETAILS.get(game_id, _GAME_DETAILS["game-001"])
