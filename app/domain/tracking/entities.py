from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass(frozen=True)
class TrackingSession:
    id: str
    user_id: str
    game_id: str
    platform_id: str
    started_at: datetime
    ended_at: Optional[datetime]
    minutes_played: Optional[int]


@dataclass(frozen=True)
class TrackingSessionCreate:
    user_id: str
    game_id: str
    platform_id: str
    started_at: datetime
    ended_at: Optional[datetime]
