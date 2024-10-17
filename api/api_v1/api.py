from fastapi import APIRouter

from api.roles import roles
from api.routers import users

api_router = APIRouter()

# Подключение маршрутов для пользователей и ролей
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(roles.router, prefix="/roles", tags=["roles"])
