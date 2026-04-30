from app.application.ports.recommendation_repository import RecommendationRepository
from app.domain.recommendations.entities import RecommendationItem


class RecommendationService:
    def __init__(self, repository: RecommendationRepository) -> None:
        self._repository = repository

    def get_recommendations(self, user_id: str) -> list[RecommendationItem]:
        return self._repository.get_recommendations(user_id)
