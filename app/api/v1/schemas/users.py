from datetime import datetime

from pydantic import BaseModel, Field

from app.api.v1.schemas.catalog import GameSummaryResponse
from app.api.v1.schemas.common import PageResponse


class UserProfileResponse(BaseModel):
    id: str
    display_name: str
    region: str
    favorite_genres: list[str] = []
    preferred_platforms: list[str] = []


class UserLibraryItemResponse(BaseModel):
    game: GameSummaryResponse
    status: str = Field(..., description="backlog|playing|completed|dropped")
    last_played_at: datetime | None = None
    hours_played: float = 0.0


class UserLibraryResponse(PageResponse[UserLibraryItemResponse]):
    pass
