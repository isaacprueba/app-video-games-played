from typing import Protocol

from app.domain.tracking.entities import TrackingSession, TrackingSessionCreate


class TrackingRepository(Protocol):
    def create_session(self, payload: TrackingSessionCreate, minutes_played: int | None) -> TrackingSession:
        ...

    def list_sessions(self, user_id: str) -> list[TrackingSession]:
        ...
