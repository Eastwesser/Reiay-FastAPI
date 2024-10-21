from fastapi import WebSocket, WebSocketDisconnect

from main import app
from redis.redis import save_message_in_cache


@app.websocket("/ws/{chat_id}")
async def websocket_endpoint(websocket: WebSocket, chat_id: int):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            # Отправляем уведомления всем пользователям, подписанным на этот чат
            await websocket.send_text(f"Message in chat {chat_id}: {data}")
            save_message_in_cache(chat_id, data)  # Сохраняем сообщение в Redis
    except WebSocketDisconnect:
        print(f"Client disconnected from chat {chat_id}")
    finally:
        await websocket.close()  # Закрытие WebSocket
