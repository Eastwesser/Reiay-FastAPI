from fastapi import APIRouter

from api.api_reiay.views import (
    roles_views,
    users_views,
    chats_views,
    messages_views,
    rooms_views,
)

# Основной роутер для api_reiay
api_router = APIRouter()

# Маршруты для пользователей, ролей и т.д.
api_router.include_router(users_views.router, prefix="/users", tags=["Users"])
api_router.include_router(roles_views.router, prefix="/roles", tags=["Roles"])
api_router.include_router(chats_views.router, prefix="/chat", tags=["Chat"])
api_router.include_router(messages_views.router, prefix="/message", tags=["Message"])
api_router.include_router(rooms_views.router, prefix="/room", tags=["Room"])
