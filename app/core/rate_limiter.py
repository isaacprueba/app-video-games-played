import time
from collections import defaultdict, deque
from typing import Deque

from fastapi import HTTPException, Request, status


class RateLimiter:
    def __init__(self, limit_per_minute: int, enabled: bool = True) -> None:
        self.limit_per_minute = limit_per_minute
        self.enabled = enabled
        self._hits: dict[str, Deque[float]] = defaultdict(deque)

    def __call__(self, request: Request) -> None:
        if not self.enabled:
            return
        now = time.time()
        key = request.client.host if request.client else "unknown"
        hits = self._hits[key]
        window_start = now - 60
        while hits and hits[0] < window_start:
            hits.popleft()
        if len(hits) >= self.limit_per_minute:
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="Rate limit exceeded.",
            )
        hits.append(now)
