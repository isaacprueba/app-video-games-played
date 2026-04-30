from dataclasses import dataclass


@dataclass(frozen=True)
class IntegrationSource:
    id: str
    name: str
    category: str
