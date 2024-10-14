from api.api_v1.api import api_router
from fastapi import FastAPI, WebSocket
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from api.redis import Redis

# Настройки базы данных
DATABASE_URL = "postgresql://user:password@localhost/dbname"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Инициализация приложения
app = FastAPI()

# Подключение роутов API
app.include_router(api_router)

# Redis для кэша и временных данных
redis = Redis(host='localhost', port=6379, db=0)


# Зависимость для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# WebSocket для чатов
@app.websocket("/ws/{chat_id}")
async def websocket_endpoint(websocket: WebSocket, chat_id: int):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message from {chat_id}: {data}")
