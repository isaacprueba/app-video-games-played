from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional


@dataclass(frozen=True)
class Guide:
    id: str
    game_id: str
    title: str
    difficulty: str
    tags: List[str]


@dataclass(frozen=True)
class Entity:
    id: str
    game_id: str
    name: str
    role: str
    strategy_hint: str


@dataclass(frozen=True)
class NewsItem:
    id: str
    title: str
    source: str
    published_at: datetime
    summary: str


@dataclass(frozen=True)
class EventItem:
    id: str
    game_id: str
    title: str
    starts_at: datetime
    ends_at: Optional[datetime]
    category: str
