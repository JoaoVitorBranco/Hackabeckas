from fastapi import FastAPI, Request
from src.modules.create_order.app.create_order_presenter import create_order_presenter
from src.modules.get_order.get_order_presenter import get_order_presenter

app = FastAPI()

@app.get("/get_order/")
def get_order(id_order: int = None):
    request = {
        "body":{},
        "headers": {},
        "query_params": {
            "id_order": id_order
        }
    }
    response = get_order_presenter(request, None)
    return response

@app.post("/create_order/")
async def create_order(request: Request):
    body = await request.json()
    request_json = {
        "body":body
    }
    
    response = create_order_presenter(request_json, None)
    return response