# WebSocket для обработки сообщений
from fastapi import WebSocket, WebSocketDisconnect

from main import app


# WebSocket для чатов
@app.websocket("/ws/{chat_id}")
async def websocket_endpoint(websocket: WebSocket, chat_id: int):
    """WebSocket для работы с реальными чатами."""
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()  # Получение сообщений от клиента
            await websocket.send_text(f"New message in chat {chat_id}: {data}")  # Ответ клиенту
    except WebSocketDisconnect:
        print(f"Client disconnected from chat {chat_id}")
