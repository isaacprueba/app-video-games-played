from app.domain.integrations.entities import IntegrationSource


class ExternalCatalogClient:
    def list_sources(self) -> list[IntegrationSource]:
        return [
            IntegrationSource(id="igdb", name="IGDB", category="catalog"),
            IntegrationSource(id="rawg", name="RAWG", category="catalog"),
        ]
