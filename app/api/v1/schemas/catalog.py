from pydantic import BaseModel, Field

from app.api.v1.schemas.common import PageResponse


class PlatformResponse(BaseModel):
    id: str
    name: str
    family: str | None = None


class GameSummaryResponse(BaseModel):
    id: str
    title: str
    platforms: list[PlatformResponse]
    genres: list[str] = []
    release_year: int | None = None
    publisher: str | None = None


class GameDetailResponse(GameSummaryResponse):
    description: str | None = None
    multiplayer_modes: list[str] = []
    entities_count: int = 0
    guides_count: int = 0


class GameSearchResponse(PageResponse[GameSummaryResponse]):
    pass
