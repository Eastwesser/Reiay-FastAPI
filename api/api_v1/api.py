from fastapi import APIRouter

from api.routers import users, roles

# Основной роутер для версий API
api_router = APIRouter()

# Подключаем роуты для пользователей и ролей
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(roles.router, prefix="/roles", tags=["Roles"])
