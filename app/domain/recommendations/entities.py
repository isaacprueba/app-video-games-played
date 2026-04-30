from dataclasses import dataclass


@dataclass(frozen=True)
class RecommendationItem:
    user_id: str
    game_id: str
    reason: str
    confidence: float
