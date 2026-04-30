from app.application.ports.tracking_repository import TrackingRepository
from app.domain.tracking.entities import TrackingSession, TrackingSessionCreate


class TrackingService:
    def __init__(self, repository: TrackingRepository) -> None:
        self._repository = repository

    def create_session(self, payload: TrackingSessionCreate) -> TrackingSession:
        if payload.ended_at and payload.ended_at < payload.started_at:
            raise ValueError("ended_at must be after started_at")
        minutes_played = None
        if payload.ended_at:
            delta = payload.ended_at - payload.started_at
            minutes_played = max(int(delta.total_seconds() // 60), 0)
        return self._repository.create_session(payload, minutes_played)

    def list_sessions(self, user_id: str) -> list[TrackingSession]:
        return self._repository.list_sessions(user_id)
