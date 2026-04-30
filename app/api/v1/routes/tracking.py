from fastapi import APIRouter, Depends, HTTPException, status

from app.api.dependencies import get_tracking_service
from app.api.v1.schemas.tracking import TrackingSessionCreateRequest, TrackingSessionResponse
from app.application.services.tracking_service import TrackingService
from app.domain.tracking.entities import TrackingSessionCreate

router = APIRouter()


@router.post("/sessions", response_model=TrackingSessionResponse)
def create_tracking_session(
    payload: TrackingSessionCreateRequest,
    service: TrackingService = Depends(get_tracking_service),
) -> TrackingSessionResponse:
    try:
        session = service.create_session(
            TrackingSessionCreate(
                user_id=payload.user_id,
                game_id=payload.game_id,
                platform_id=payload.platform_id,
                started_at=payload.started_at,
                ended_at=payload.ended_at,
            )
        )
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    return TrackingSessionResponse(**session.__dict__)


@router.get("/sessions/{user_id}", response_model=list[TrackingSessionResponse])
def list_sessions(
    user_id: str,
    service: TrackingService = Depends(get_tracking_service),
) -> list[TrackingSessionResponse]:
    sessions = service.list_sessions(user_id)
    return [TrackingSessionResponse(**session.__dict__) for session in sessions]
