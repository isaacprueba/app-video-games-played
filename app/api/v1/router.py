from fastapi import APIRouter

from app.api.v1.routes import catalog, content, recommendations, tracking, users

v1_router = APIRouter()

v1_router.include_router(catalog.router, prefix="/games", tags=["games"])
v1_router.include_router(users.router, prefix="/users", tags=["users"])
v1_router.include_router(tracking.router, prefix="/tracking", tags=["tracking"])
v1_router.include_router(recommendations.router, prefix="/recommendations", tags=["recommendations"])
v1_router.include_router(content.router, prefix="/content", tags=["content"])
