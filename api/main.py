from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from core.db_helper import engine
from reiay.routers.api_routers import api_router

# Инициализация приложения FastAPI
app = FastAPI()

# Создание сессии базы данных
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# Подключаем роуты с префиксом /api/reiay
app.include_router(
    api_router,
    prefix="/api/reiay",
    tags=["reiai"],
)

# Запуск приложения
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
