from datetime import datetime

from pydantic import BaseModel


class GuideResponse(BaseModel):
    id: str
    game_id: str
    title: str
    difficulty: str
    tags: list[str] = []


class EntityResponse(BaseModel):
    id: str
    game_id: str
    name: str
    role: str
    strategy_hint: str


class NewsResponse(BaseModel):
    id: str
    title: str
    source: str
    published_at: datetime
    summary: str


class EventResponse(BaseModel):
    id: str
    game_id: str
    title: str
    starts_at: datetime
    ends_at: datetime | None = None
    category: str
