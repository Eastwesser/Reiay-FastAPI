from fastapi import FastAPI, WebSocket
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from api.api_v1.api import api_router
from api.database.db_configs import engine

# Настройки базы данных
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# Инициализация FastAPI
app = FastAPI()

# Подключение роутеров
app.include_router(api_router)


# Зависимость для получения сессии базы данных
async def get_db():
    async with SessionLocal() as session:
        yield session


# WebSocket для чатов
@app.websocket("/ws/{chat_id}")
async def websocket_endpoint(websocket: WebSocket, chat_id: int):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message from {chat_id}: {data}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        await websocket.close()
