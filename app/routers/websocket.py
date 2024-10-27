from fastapi import APIRouter, WebSocket

router = APIRouter()

# Ejemplo de endpoint de WebSocket
@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_text("Conexión WebSocket establecida")
    await websocket.close()
