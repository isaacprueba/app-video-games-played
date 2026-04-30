from datetime import datetime, timezone, timedelta

from fastapi import APIRouter, Query

from app.schemas import EntitySummary, EventItem, GuideSummary, NewsItem

router = APIRouter()


@router.get("/news", response_model=list[NewsItem])
def list_news() -> list[NewsItem]:
    return [
        NewsItem(
            id="news-001",
            title="Temporada estelar: nuevas misiones",
            source="Game Atlas",
            published_at=datetime.now(timezone.utc) - timedelta(days=1),
            summary="Nueva oleada de desafíos y recompensas en títulos sci-fi.",
        )
    ]


@router.get("/events", response_model=list[EventItem])
def list_events(game_id: str | None = Query(default=None)) -> list[EventItem]:
    event = EventItem(
        id="event-001",
        game_id=game_id or "game-001",
        title="Festival de gremios",
        starts_at=datetime.now(timezone.utc) + timedelta(days=3),
        ends_at=datetime.now(timezone.utc) + timedelta(days=7),
        category="community",
    )
    return [event]


@router.get("/guides", response_model=list[GuideSummary])
def list_guides(game_id: str | None = Query(default=None)) -> list[GuideSummary]:
    return [
        GuideSummary(
            id="guide-001",
            game_id=game_id or "game-001",
            title="Build inicial para novatos",
            difficulty="beginner",
            tags=["build", "early-game"],
        )
    ]


@router.get("/entities", response_model=list[EntitySummary])
def list_entities(game_id: str | None = Query(default=None)) -> list[EntitySummary]:
    return [
        EntitySummary(
            id="entity-001",
            game_id=game_id or "game-001",
            name="Astra",
            role="NPC",
            strategy_hint="Prioriza misiones de exploración para desbloquear habilidades.",
        )
    ]
