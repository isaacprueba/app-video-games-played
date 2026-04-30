from typing import Protocol

from app.domain.recommendations.entities import RecommendationItem


class RecommendationRepository(Protocol):
    def get_recommendations(self, user_id: str) -> list[RecommendationItem]:
        raise NotImplementedError
