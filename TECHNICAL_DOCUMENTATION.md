# Documentación técnica integral - App Video Games Played

## Objetivo
Construir una plataforma escalable para descubrir, trackear y potenciar la experiencia de videojuegos en múltiples plataformas, con arquitectura modular, contratos API versionados y foco en rendimiento, seguridad y mantenibilidad.

## Alcance funcional prioritario
- Catálogo con búsqueda avanzada por plataforma, género y región.
- Perfil de usuario, biblioteca y preferencias.
- Tracking de sesiones con métricas de tiempo.
- Recomendaciones personalizadas.
- Contenido editorial: noticias, eventos, guías y entidades del juego.
- Integraciones externas para catálogos y noticias.
- Analítica de uso y observabilidad.

## Requisitos no funcionales
- Escalabilidad horizontal por dominios.
- Rendimiento con caché y paginación.
- Seguridad con autenticación, autorización y rate limiting.
- Observabilidad con logging estructurado y métricas.
- Configuración por entorno y despliegue reproducible.

## Arquitectura y capas
Monolito modular con límites de contexto claros y capas desacopladas:
- **API**: contratos HTTP y validación de entrada/salida.
- **Aplicación**: orquestación de casos de uso.
- **Dominio**: entidades y reglas de negocio.
- **Infraestructura**: repositorios, caché, integraciones, observabilidad.
- **Datos**: datasets, modelos persistentes y migraciones (cuando aplique).

## Contextos principales
Catálogo, Usuarios/Perfil, Tracking, Recomendaciones, Contenido, Eventos, Integraciones, Analítica.

## Estructura del repositorio
```
app/
  api/
    v1/
      routes/
      schemas/
  application/
    ports/
    services/
  core/
  data/
  domain/
  infrastructure/
  main.py
tests/
  unit/
  integration/
  contract/
requirements.txt
requirements-dev.txt
```

## Contratos API (v1)
Prefijo: `/api/v1`
- `GET /games/search`
- `GET /games/{id}`
- `GET /users/{id}/profile`
- `GET /users/{id}/library`
- `POST /tracking/sessions`
- `GET /tracking/sessions/{user_id}`
- `GET /recommendations/{user_id}`
- `GET /content/news`
- `GET /content/events`
- `GET /content/guides`
- `GET /content/entities`
- `GET /health`

## Modelo de datos (conceptual)
- **Game**: id, title, description, platforms, genres, release_year, publisher.
- **Platform**: id, name, family.
- **UserProfile**: id, display_name, region, favorite_genres, preferred_platforms.
- **UserLibraryItem**: user_id, game_id, status, last_played_at, hours_played.
- **TrackingSession**: id, user_id, game_id, platform_id, started_at, ended_at, minutes_played.
- **RecommendationItem**: user_id, game_id, reason, confidence.
- **Guide**: id, game_id, title, difficulty, tags.
- **Entity**: id, game_id, name, role, strategy_hint.
- **NewsItem**: id, title, source, published_at, summary.
- **EventItem**: id, game_id, title, starts_at, ends_at, category.

## Flujos clave
1. **Búsqueda de catálogo**: API -> Servicio -> Repositorio -> Cache -> Respuesta paginada.
2. **Tracking**: API valida -> Servicio calcula duración -> Repositorio persiste.
3. **Recomendaciones**: API -> Servicio -> Repositorio -> Enriquecimiento con catálogo.

## Seguridad
- Header `X-API-Key` opcional por entorno.
- Rate limiting configurable por IP.

## Rendimiento y escalabilidad
- Paginación estandarizada en listados.
- Caché en consultas de catálogo y perfiles.
- Preparado para migrar repositorios a DB real y separar dominios.

## Observabilidad
- Logging de requests con latencia y status.
- Espacio para métricas y trazas en infraestructura.

## Configuración por entorno
Variables principales:
- `APP_NAME`, `APP_VERSION`, `ENVIRONMENT`
- `API_PREFIX`
- `API_KEY`
- `RATE_LIMIT_PER_MINUTE`, `ENABLE_RATE_LIMIT`
- `CACHE_TTL_SECONDS`, `DEFAULT_PAGE_SIZE`, `MAX_PAGE_SIZE`

## Desarrollo local
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

## Pruebas
- Unitarias, integración y contractuales en `tests/`.
```bash
pytest
```

## Despliegue
- Ejecutar con `uvicorn app.main:app`.
- Preparar variables de entorno y ajustar rate limiting/caché según el entorno.

## Contribución
- Respetar capas y límites de contexto.
- Añadir pruebas para cambios en dominios o API.
- Mantener consistencia en contratos versionados.
