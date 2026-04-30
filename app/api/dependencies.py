from functools import lru_cache

from app.application.services.catalog_service import CatalogService
from app.application.services.content_service import ContentService
from app.application.services.recommendation_service import RecommendationService
from app.application.services.tracking_service import TrackingService
from app.application.services.user_service import UserService
from app.core.config import settings
from app.core.rate_limiter import RateLimiter
from app.infrastructure.cache.memory import InMemoryCache
from app.infrastructure.repositories.in_memory_catalog import InMemoryCatalogRepository
from app.infrastructure.repositories.in_memory_content import InMemoryContentRepository
from app.infrastructure.repositories.in_memory_recommendations import InMemoryRecommendationRepository
from app.infrastructure.repositories.in_memory_tracking import InMemoryTrackingRepository
from app.infrastructure.repositories.in_memory_users import InMemoryUserRepository


@lru_cache
def get_cache() -> InMemoryCache:
    return InMemoryCache()


@lru_cache
def get_rate_limiter() -> RateLimiter:
    return RateLimiter(
        limit_per_minute=settings.rate_limit_per_minute,
        enabled=settings.enable_rate_limit,
    )


@lru_cache
def get_catalog_service() -> CatalogService:
    return CatalogService(InMemoryCatalogRepository(), get_cache())


@lru_cache
def get_user_service() -> UserService:
    return UserService(InMemoryUserRepository(), get_cache())


@lru_cache
def get_tracking_service() -> TrackingService:
    return TrackingService(InMemoryTrackingRepository())


@lru_cache
def get_recommendation_service() -> RecommendationService:
    return RecommendationService(InMemoryRecommendationRepository())


@lru_cache
def get_content_service() -> ContentService:
    return ContentService(InMemoryContentRepository())
