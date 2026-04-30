import pytest


@pytest.mark.anyio
async def test_health_contract(client) -> None:
    response = await client.get("/health")
    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"
    assert "environment" in payload
    assert "version" in payload


@pytest.mark.anyio
async def test_search_games_contract(client) -> None:
    response = await client.get("/api/v1/games/search", params={"q": "Ne"})
    assert response.status_code == 200
    payload = response.json()
    assert "items" in payload
    assert "meta" in payload
    assert isinstance(payload["items"], list)


@pytest.mark.anyio
async def test_user_profile_contract(client) -> None:
    response = await client.get("/api/v1/users/user-001/profile")
    assert response.status_code == 200
    payload = response.json()
    assert payload["id"] == "user-001"
