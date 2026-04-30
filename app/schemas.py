from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class Platform(BaseModel):
    id: str
    name: str


class GameSummary(BaseModel):
    id: str
    title: str
    platforms: List[Platform]
    genres: List[str] = []
    release_year: Optional[int] = None


class GameDetail(GameSummary):
    description: Optional[str] = None
    multiplayer_modes: List[str] = []
    entities_count: int = 0
    guides_count: int = 0


class UserProfile(BaseModel):
    id: str
    display_name: str
    region: str
    favorite_genres: List[str] = []
    preferred_platforms: List[str] = []


class UserLibraryItem(BaseModel):
    game: GameSummary
    status: str = Field(..., description="backlog|playing|completed|dropped")
    last_played_at: Optional[datetime] = None
    hours_played: float = 0.0


class RecommendationItem(BaseModel):
    game: GameSummary
    reason: str
    confidence: float = Field(ge=0, le=1)


class TrackingSessionCreate(BaseModel):
    user_id: str
    game_id: str
    platform_id: str
    started_at: datetime
    ended_at: Optional[datetime] = None


class TrackingSession(BaseModel):
    id: str
    user_id: str
    game_id: str
    platform_id: str
    started_at: datetime
    ended_at: Optional[datetime] = None
    minutes_played: Optional[int] = None


class GuideSummary(BaseModel):
    id: str
    game_id: str
    title: str
    difficulty: str
    tags: List[str] = []


class EntitySummary(BaseModel):
    id: str
    game_id: str
    name: str
    role: str
    strategy_hint: str


class NewsItem(BaseModel):
    id: str
    title: str
    source: str
    published_at: datetime
    summary: str


class EventItem(BaseModel):
    id: str
    game_id: str
    title: str
    starts_at: datetime
    ends_at: Optional[datetime] = None
    category: str
