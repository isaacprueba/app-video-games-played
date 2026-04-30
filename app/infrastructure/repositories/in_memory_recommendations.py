from app.application.ports.recommendation_repository import RecommendationRepository
from app.data.sample_data import RECOMMENDATIONS
from app.domain.recommendations.entities import RecommendationItem


class InMemoryRecommendationRepository(RecommendationRepository):
    def __init__(self) -> None:
        self._recommendations = {user_id: list(items) for user_id, items in RECOMMENDATIONS.items()}

    def get_recommendations(self, user_id: str) -> list[RecommendationItem]:
        return list(self._recommendations.get(user_id, []))
