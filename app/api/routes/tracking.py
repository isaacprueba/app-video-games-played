from datetime import datetime, timezone
from uuid import uuid4

from fastapi import APIRouter

from app.schemas import TrackingSession, TrackingSessionCreate

router = APIRouter()


@router.post("/sessions", response_model=TrackingSession)
def create_tracking_session(payload: TrackingSessionCreate) -> TrackingSession:
    minutes_played = None
    if payload.ended_at:
        delta = payload.ended_at - payload.started_at
        minutes_played = max(int(delta.total_seconds() // 60), 0)
    return TrackingSession(
        id=str(uuid4()),
        user_id=payload.user_id,
        game_id=payload.game_id,
        platform_id=payload.platform_id,
        started_at=payload.started_at,
        ended_at=payload.ended_at,
        minutes_played=minutes_played,
    )


@router.get("/sessions/{user_id}", response_model=list[TrackingSession])
def list_sessions(user_id: str) -> list[TrackingSession]:
    now = datetime.now(timezone.utc)
    return [
        TrackingSession(
            id=str(uuid4()),
            user_id=user_id,
            game_id="game-001",
            platform_id="pc",
            started_at=now,
            ended_at=None,
            minutes_played=None,
        )
    ]
