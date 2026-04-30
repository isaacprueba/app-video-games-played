# App Video Games Played

Plataforma inteligente para descubrir, trackear y potenciar la experiencia de cualquier videojuego en PC, móvil y otras plataformas.

## Alcance funcional mínimo
- Catálogo global con búsqueda avanzada por plataforma, género y región.
- Tracking de sesiones y progreso por usuario.
- Perfiles con preferencias, historial y biblioteca.
- Recomendaciones inteligentes y personalizadas.
- Noticias, eventos y actualizaciones por juego.
- Guías, estrategias, builds y tips por rol/estilo de juego.
- Entidades del juego: personajes, NPC, ítems, habilidades y sus sinergias.

## Arquitectura objetivo
- **Monolito modular inicial** con límites de contexto claros y escalable a microservicios.
- **Contextos principales**: Catálogo, Perfil/Usuario, Tracking, Recomendaciones, Contenido/Guías, Eventos/Noticias, Integraciones, Analítica.
- **Integraciones**: APIs externas para catálogos globales, noticias y estadísticas.
- **Estrategia de escalado**: separación por dominios cuando el tráfico o la complejidad lo justifique.

## Fuentes de datos (sugeridas)
- Catálogo global: IGDB, RAWG, Steam, PlayStation, Nintendo.
- Noticias/Eventos: feeds oficiales, RSS y publicaciones de comunidades verificadas.
- Estrategias/Guías: curación interna + fuentes con licencia.

## Modelo de datos inicial
- **Game**: id, título, descripción, plataformas, géneros, release, publisher.
- **Platform**: id, nombre, familia.
- **UserProfile**: id, región, preferencias, disponibilidad.
- **UserLibrary**: usuario, juego, estado, progreso, horas.
- **TrackingSession**: usuario, juego, plataforma, inicio, fin, duración.
- **Guide**: juego, título, dificultad, tags, estrategia.
- **Entity**: juego, nombre, rol, sinergias, tips.
- **News/Event**: juego, título, fechas, fuente, resumen.

## Módulos y APIs (v1)
- **Catálogo**: `GET /games/search`, `GET /games/{id}`
- **Usuarios**: `GET /users/{id}/profile`, `GET /users/{id}/library`
- **Tracking**: `POST /tracking/sessions`, `GET /tracking/sessions/{user_id}`
- **Recomendaciones**: `GET /recommendations/{user_id}`
- **Contenido**: `GET /content/news`, `GET /content/events`, `GET /content/guides`, `GET /content/entities`
- **Salud**: `GET /health`

## Stack base (propuesto)
- Backend: **FastAPI** + Python 3.11+
- DB relacional: **PostgreSQL**
- Cache/colas: **Redis**
- Búsqueda: **OpenSearch / Elasticsearch**
- Procesamiento asíncrono: **Celery / RQ**
- Observabilidad: OpenTelemetry + métricas

## Estructura del repositorio
```
app/
  api/
    routes/
  core/
  main.py
  schemas.py
requirements.txt
```

## Desarrollo local
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Roadmap (iteraciones)
1. **Base API**: scaffolding, modelos, healthcheck, endpoints stub.
2. **Catálogo + Búsqueda**: ingesta inicial y filtros.
3. **Tracking + Perfil**: sesiones, biblioteca, progreso.
4. **Recomendaciones**: motor híbrido + feedback.
5. **Contenido**: guías, estrategias, eventos y noticias.
