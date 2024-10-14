from fastapi import APIRouter

from api.routers import users
from api.roles import roles

api_router = APIRouter()

# Подключение маршрутов для пользователей и ролей
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(roles.router, prefix="/roles", tags=["roles"])
