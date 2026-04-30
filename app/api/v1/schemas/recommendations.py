from pydantic import BaseModel, Field

from app.api.v1.schemas.catalog import GameSummaryResponse


class RecommendationResponse(BaseModel):
    game: GameSummaryResponse
    reason: str
    confidence: float = Field(ge=0, le=1)
