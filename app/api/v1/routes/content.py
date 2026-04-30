from fastapi import APIRouter, Depends, Query

from app.api.dependencies import get_content_service
from app.api.v1.schemas.content import EntityResponse, EventResponse, GuideResponse, NewsResponse
from app.application.services.content_service import ContentService
from app.domain.content.entities import Entity, EventItem, Guide, NewsItem

router = APIRouter()


def _news_response(item: NewsItem) -> NewsResponse:
    return NewsResponse(**item.__dict__)


def _event_response(item: EventItem) -> EventResponse:
    return EventResponse(**item.__dict__)


def _guide_response(item: Guide) -> GuideResponse:
    return GuideResponse(**item.__dict__)


def _entity_response(item: Entity) -> EntityResponse:
    return EntityResponse(**item.__dict__)


@router.get("/news", response_model=list[NewsResponse])
def list_news(service: ContentService = Depends(get_content_service)) -> list[NewsResponse]:
    return [_news_response(item) for item in service.list_news()]


@router.get("/events", response_model=list[EventResponse])
def list_events(
    game_id: str | None = Query(default=None),
    service: ContentService = Depends(get_content_service),
) -> list[EventResponse]:
    return [_event_response(item) for item in service.list_events(game_id)]


@router.get("/guides", response_model=list[GuideResponse])
def list_guides(
    game_id: str | None = Query(default=None),
    service: ContentService = Depends(get_content_service),
) -> list[GuideResponse]:
    return [_guide_response(item) for item in service.list_guides(game_id)]


@router.get("/entities", response_model=list[EntityResponse])
def list_entities(
    game_id: str | None = Query(default=None),
    service: ContentService = Depends(get_content_service),
) -> list[EntityResponse]:
    return [_entity_response(item) for item in service.list_entities(game_id)]
