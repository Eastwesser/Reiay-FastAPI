from fastapi import APIRouter

from api.roles import roles
from api.routers import users

# Основной роутер API
api_router = APIRouter()

# Подключение маршрутов
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(roles.router, prefix="/roles", tags=["Roles"])
