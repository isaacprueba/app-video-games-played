from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class Platform:
    id: str
    name: str
    family: Optional[str] = None


@dataclass(frozen=True)
class Game:
    id: str
    title: str
    description: Optional[str]
    platforms: List[Platform]
    genres: List[str]
    release_year: Optional[int]
    publisher: Optional[str]


@dataclass(frozen=True)
class GameDetail(Game):
    multiplayer_modes: List[str]
    entities_count: int
    guides_count: int
