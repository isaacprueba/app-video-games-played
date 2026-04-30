from datetime import datetime

from pydantic import BaseModel


class TrackingSessionCreateRequest(BaseModel):
    user_id: str
    game_id: str
    platform_id: str
    started_at: datetime
    ended_at: datetime | None = None


class TrackingSessionResponse(BaseModel):
    id: str
    user_id: str
    game_id: str
    platform_id: str
    started_at: datetime
    ended_at: datetime | None = None
    minutes_played: int | None = None
