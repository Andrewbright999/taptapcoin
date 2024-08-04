from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect, Cookie, Depends, Query, WebSocketException, status
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from economic_core import on_tap, on_buy_upgrade, get_cost_upgrade
from json_adapter import get_user_data
from pprint import pprint

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

json_path = "balance.json"
    
class ConnectionManager:
    def __init__(self) -> None:
        self.active_connections: list[WebSocket] = []
        
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
    
    async def disconect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
 
    async def send_user_data(self, websocket: WebSocket, id):
        user_data = get_user_data(id)
        await websocket.send_json(user_data)
        return user_data
        
    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)
            
manager = ConnectionManager()

@app.get("/")
def get_admin_page(request: Request) -> HTMLResponse:
    """Главная страница"""
    return templates.TemplateResponse("index.html", {"request": request})


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
    # balance = await manager.read_balance(websocket)
        while True:
            data = await websocket.receive_json()
            id = int(data["id"])
            pprint(data)
            if data["event"] == "click":
                on_tap(id)
            if data["event"] == "buy_upgrade":
                on_buy_upgrade(id)
            await manager.send_user_data(websocket,id)
            # balance = await manager.read_balance(websocket)
            # print(f"In loop{balance}")
            # write_balance_json(balance)
            # await manager.read_balance(websocket)
    except WebSocketDisconnect:
        manager.disconect(websocket)
        
    