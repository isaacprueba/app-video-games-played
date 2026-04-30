from datetime import datetime, timedelta, timezone

from app.application.services.tracking_service import TrackingService
from app.domain.tracking.entities import TrackingSessionCreate
from app.infrastructure.repositories.in_memory_tracking import InMemoryTrackingRepository


def test_create_tracking_session_calculates_minutes() -> None:
    repository = InMemoryTrackingRepository()
    service = TrackingService(repository)
    start = datetime.now(timezone.utc) - timedelta(minutes=45)
    end = datetime.now(timezone.utc)
    session = service.create_session(
        TrackingSessionCreate(
            user_id="user-001",
            game_id="game-001",
            platform_id="pc",
            started_at=start,
            ended_at=end,
        )
    )
    assert session.minutes_played == 45


def test_create_tracking_session_without_end_time() -> None:
    repository = InMemoryTrackingRepository()
    service = TrackingService(repository)
    start = datetime.now(timezone.utc)
    session = service.create_session(
        TrackingSessionCreate(
            user_id="user-001",
            game_id="game-001",
            platform_id="pc",
            started_at=start,
            ended_at=None,
        )
    )
    assert session.minutes_played is None


def test_create_tracking_session_zero_minutes() -> None:
    repository = InMemoryTrackingRepository()
    service = TrackingService(repository)
    start = datetime.now(timezone.utc)
    session = service.create_session(
        TrackingSessionCreate(
            user_id="user-001",
            game_id="game-001",
            platform_id="pc",
            started_at=start,
            ended_at=start,
        )
    )
    assert session.minutes_played == 0
