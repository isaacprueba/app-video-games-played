from app.api.v1.schemas.catalog import GameDetailResponse, GameSummaryResponse, PlatformResponse
from app.domain.catalog.entities import Game, GameDetail, Platform


def to_platform_response(platform: Platform) -> PlatformResponse:
    return PlatformResponse(id=platform.id, name=platform.name, family=platform.family)


def to_game_summary_response(game: Game) -> GameSummaryResponse:
    return GameSummaryResponse(
        id=game.id,
        title=game.title,
        platforms=[to_platform_response(platform) for platform in game.platforms],
        genres=game.genres,
        release_year=game.release_year,
        publisher=game.publisher,
    )


def to_game_detail_response(game: GameDetail) -> GameDetailResponse:
    return GameDetailResponse(
        **to_game_summary_response(game).model_dump(),
        description=game.description,
        multiplayer_modes=game.multiplayer_modes,
        entities_count=game.entities_count,
        guides_count=game.guides_count,
    )


def game_summary_from_detail(detail: GameDetail | None, fallback_id: str) -> GameSummaryResponse:
    if not detail:
        return GameSummaryResponse(
            id=fallback_id,
            title="Unknown",
            platforms=[],
            genres=[],
            release_year=None,
            publisher=None,
        )
    return to_game_summary_response(detail)
