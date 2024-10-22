from fastapi import FastAPI
from fastapi.middleware import Middleware
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from api.core.db_helper import engine
from api.i18n.i18n_helper import translate
from api.i18n.middleware import LocaleMiddleware
from api.reiay.routers.api_routers import api_router

app = FastAPI(middleware=[Middleware(LocaleMiddleware)])


@app.get("/greeting/")
async def get_greeting():
    return {"message": translate('greeting.hello')}


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
    tags=["reiay"],
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
