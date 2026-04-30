from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional


@dataclass(frozen=True)
class UserProfile:
    id: str
    display_name: str
    region: str
    favorite_genres: List[str]
    preferred_platforms: List[str]


@dataclass(frozen=True)
class UserLibraryItem:
    user_id: str
    game_id: str
    status: str
    last_played_at: Optional[datetime]
    hours_played: float
