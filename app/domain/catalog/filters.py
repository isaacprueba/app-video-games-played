from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class GameSearchFilters:
    query: str
    platform: Optional[str] = None
    genre: Optional[str] = None
    region: Optional[str] = None
