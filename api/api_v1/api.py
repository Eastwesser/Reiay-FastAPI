from fastapi import APIRouter

from api.routers import users, roles  # Импортируем роутеры для пользователей и ролей

# Создаем основной роутер для API V1
api_router = APIRouter()

# Подключаем маршруты для пользователей и ролей
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(roles.router, prefix="/roles", tags=["Roles"])
