from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_websocket():
    with client.websocket_connect("/ws/1") as websocket:
        websocket.send_text("Hello, WebSocket!")
        data = websocket.receive_text()
        assert data == "Message in chat 1: Hello, WebSocket!"
