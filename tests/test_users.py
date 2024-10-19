import pytest
from httpx import AsyncClient

from api.main import app


@pytest.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


@pytest.mark.asyncio
async def test_register_user(client: AsyncClient):
    response = await client.post("/api/v1/users/register", json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "testuser"


@pytest.mark.asyncio
async def test_login_user(client: AsyncClient):
    await client.post("/api/v1/users/register", json={"username": "testuser", "password": "testpass"})
    response = await client.post("/api/v1/users/login", json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Login successful"


@pytest.mark.asyncio
async def test_register_existing_user(client: AsyncClient):
    # Регистрируем нового пользователя
    await client.post("/api/v1/users/register", json={"username": "testuser", "password": "testpass"})
    # Попытка повторной регистрации
    response = await client.post("/api/v1/users/register", json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 400
    data = response.json()
    assert data["detail"] == "Username already registered"
