import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_health_check(client: AsyncClient):
    response = await client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "db": "connected"}

@pytest.mark.asyncio
async def test_register_user(client: AsyncClient):
    payload = {
        "first_name": "TestUser",
        "last_name": "Testov",
        "telegram_id": 12345
    }
    response = await client.post("/api/v1/users/register", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["first_name"] == "TestUser"
    assert data["id"] is not None

@pytest.mark.asyncio
async def test_check_user_exists(client: AsyncClient):
    response = await client.get("/api/v1/users/check", params={"telegram_id": 12345})
    assert response.status_code == 200
    assert response.json()["telegram_id"] == 12345

@pytest.mark.asyncio
async def test_check_user_not_found(client: AsyncClient):
    response = await client.get("/api/v1/users/check", params={"telegram_id": 999999})
    assert response.status_code == 404

@pytest.mark.asyncio
async def test_add_score(client: AsyncClient):
    payload = {
        "subject": "informatics",
        "score": 85,
        "user_telegram_id": 12345
    }
    response = await client.post("/api/v1/scores/", json=payload)
    assert response.status_code == 200
    assert response.json()["score"] == 85

@pytest.mark.asyncio
async def test_view_scores(client: AsyncClient):
    response = await client.get("/api/v1/scores/", params={"telegram_id": 12345})
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert data[0]["subject"] == "informatics"