from uuid import uuid4

from app.application.ports.tracking_repository import TrackingRepository
from app.data.sample_data import TRACKING_SESSIONS
from app.domain.tracking.entities import TrackingSession, TrackingSessionCreate


class InMemoryTrackingRepository(TrackingRepository):
    def __init__(self) -> None:
        self._sessions = {user_id: list(items) for user_id, items in TRACKING_SESSIONS.items()}

    def create_session(self, payload: TrackingSessionCreate, minutes_played: int | None) -> TrackingSession:
        session = TrackingSession(
            id=str(uuid4()),
            user_id=payload.user_id,
            game_id=payload.game_id,
            platform_id=payload.platform_id,
            started_at=payload.started_at,
            ended_at=payload.ended_at,
            minutes_played=minutes_played,
        )
        self._sessions.setdefault(payload.user_id, []).append(session)
        return session

    def list_sessions(self, user_id: str) -> list[TrackingSession]:
        return list(self._sessions.get(user_id, []))
