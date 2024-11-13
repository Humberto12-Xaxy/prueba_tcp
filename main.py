from fastapi import FastAPI, WebSocket, WebSocketDisconnect

import uvicorn

from connection.connection_manager import ConnectionManager

app = FastAPI()

manager = ConnectionManager()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            word_key = 'Desconexion'
            if data == word_key.upper() or data == word_key.lower() or data == word_key:
                await websocket.send_text('SERVIDOR DESCONECTADO')
                manager.disconnect(websocket)
            else:
                await websocket.send_text(data.upper() + ' CLIENTE')
    except WebSocketDisconnect:
        manager.disconnect(websocket)

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000)
