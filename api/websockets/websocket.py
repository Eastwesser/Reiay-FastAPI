from fastapi import WebSocket, WebSocketDisconnect

from main import app


@app.websocket("/ws/{chat_id}")
async def websocket_endpoint(websocket: WebSocket, chat_id: int):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"New message in chat {chat_id}: {data}")
    except WebSocketDisconnect:
        print(f"Client disconnected from chat {chat_id}")
