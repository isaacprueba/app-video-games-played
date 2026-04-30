from fastapi import APIRouter, Depends

from app.api.dependencies import get_rate_limiter
from app.api.v1.router import v1_router
from app.core.config import settings
from app.core.security import require_api_key

api_router = APIRouter()


@api_router.get("/health", tags=["system"])
def health_check() -> dict:
    return {"status": "ok", "environment": settings.environment, "version": settings.version}


api_router.include_router(
    v1_router,
    prefix=settings.api_prefix,
    dependencies=[Depends(require_api_key), Depends(get_rate_limiter)],
)
