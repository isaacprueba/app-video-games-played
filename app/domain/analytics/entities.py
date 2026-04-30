from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class UsageSnapshot:
    id: str
    collected_at: datetime
    active_users: int
    sessions_tracked: int
