from datetime import datetime, timezone
from datetime import timedelta

from app.domain.catalog.entities import Game, GameDetail, Platform
from app.domain.content.entities import Entity, EventItem, Guide, NewsItem
from app.domain.recommendations.entities import RecommendationItem
from app.domain.tracking.entities import TrackingSession
from app.domain.users.entities import UserLibraryItem, UserProfile


PLATFORMS = {
    "pc": Platform(id="pc", name="PC", family="desktop"),
    "ps5": Platform(id="ps5", name="PlayStation 5", family="console"),
    "switch": Platform(id="switch", name="Nintendo Switch", family="console"),
}

GAMES = [
    Game(
        id="game-001",
        title="Nebula Drift",
        description="Explora sectores dinámicos con naves modulares y eventos galácticos.",
        platforms=[PLATFORMS["pc"], PLATFORMS["ps5"]],
        genres=["Sci-Fi", "Roguelike"],
        release_year=2025,
        publisher="Stellar Forge",
    ),
    Game(
        id="game-002",
        title="Mythic Grove",
        description="Gestiona un bosque místico con criaturas y misiones colaborativas.",
        platforms=[PLATFORMS["switch"]],
        genres=["Adventure", "Simulation"],
        release_year=2024,
        publisher="Verdant Studios",
    ),
]

GAME_DETAILS = {
    "game-001": GameDetail(
        **GAMES[0].__dict__,
        multiplayer_modes=["co-op", "ranked"],
        entities_count=42,
        guides_count=8,
    ),
    "game-002": GameDetail(
        **GAMES[1].__dict__,
        multiplayer_modes=["local-coop"],
        entities_count=28,
        guides_count=5,
    ),
}

USER_PROFILES = {
    "user-001": UserProfile(
        id="user-001",
        display_name="Player One",
        region="LATAM",
        favorite_genres=["RPG", "Aventura"],
        preferred_platforms=["pc", "ps5"],
    )
}

USER_LIBRARY = {
    "user-001": [
        UserLibraryItem(
            user_id="user-001",
            game_id="game-001",
            status="playing",
            last_played_at=datetime.now(timezone.utc) - timedelta(hours=4),
            hours_played=12.5,
        )
    ]
}

TRACKING_SESSIONS = {
    "user-001": [
        TrackingSession(
            id="session-001",
            user_id="user-001",
            game_id="game-001",
            platform_id="pc",
            started_at=datetime.now(timezone.utc) - timedelta(hours=2),
            ended_at=None,
            minutes_played=None,
        )
    ]
}

RECOMMENDATIONS = {
    "user-001": [
        RecommendationItem(
            user_id="user-001",
            game_id="game-003",
            reason="Coincide con tu interés en cooperativo y fantasía épica.",
            confidence=0.82,
        )
    ]
}

NEWS = [
    NewsItem(
        id="news-001",
        title="Temporada estelar: nuevas misiones",
        source="Game Atlas",
        published_at=datetime.now(timezone.utc) - timedelta(days=1),
        summary="Nueva oleada de desafíos y recompensas en títulos sci-fi.",
    )
]

EVENTS = [
    EventItem(
        id="event-001",
        game_id="game-001",
        title="Festival de gremios",
        starts_at=datetime.now(timezone.utc) + timedelta(days=3),
        ends_at=datetime.now(timezone.utc) + timedelta(days=7),
        category="community",
    )
]

GUIDES = [
    Guide(
        id="guide-001",
        game_id="game-001",
        title="Build inicial para novatos",
        difficulty="beginner",
        tags=["build", "early-game"],
    )
]

ENTITIES = [
    Entity(
        id="entity-001",
        game_id="game-001",
        name="Astra",
        role="NPC",
        strategy_hint="Prioriza misiones de exploración para desbloquear habilidades.",
    )
]
