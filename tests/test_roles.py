import pytest
from httpx import AsyncClient

from api.main import app


@pytest.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


@pytest.mark.asyncio
async def test_create_role(client: AsyncClient):
    response = await client.post("/api/v1/roles/", json={"name": "admin"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "admin"


@pytest.mark.asyncio
async def test_get_roles(client: AsyncClient):
    await client.post("/api/v1/roles/", json={"name": "admin"})
    response = await client.get("/api/v1/roles/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
