from fastapi import APIRouter

from app.api.routes import content, games, recommendations, tracking, users

api_router = APIRouter()


@api_router.get("/health", tags=["system"])
def health_check() -> dict:
    return {"status": "ok"}


api_router.include_router(games.router, prefix="/games", tags=["games"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(tracking.router, prefix="/tracking", tags=["tracking"])
api_router.include_router(recommendations.router, prefix="/recommendations", tags=["recommendations"])
api_router.include_router(content.router, prefix="/content", tags=["content"])
