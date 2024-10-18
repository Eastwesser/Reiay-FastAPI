from fastapi import FastAPI, WebSocket
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from api.api_v1.api import api_router
from core.database.db_configs import engine

# Создание сессии базы данных
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# Инициализация приложения FastAPI
app = FastAPI()

# Подключаем роуты с префиксом /api/v1
app.include_router(api_router, prefix="/api/v1")


# Зависимость для получения сессии базы данных
async def get_db():
    async with SessionLocal() as session:
        yield session


# WebSocket для чатов
@app.websocket("/ws/{chat_id}")
async def websocket_endpoint(websocket: WebSocket, chat_id: int):
    """WebSocket для обработки сообщений в чатах."""
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()  # Получение сообщения
            await websocket.send_text(f"Message from {chat_id}: {data}")  # Отправка ответа
    except Exception as e:
        print(f"Error: {e}")
    finally:
        await websocket.close()  # Закрытие WebSocket


# Запуск приложения
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
