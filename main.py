from fastapi import FastAPI, Request
from pydantic import BaseModel
from src.modules.create_order.app.create_order_presenter import create_order_presenter
from src.modules.get_order.get_order_presenter import get_order_presenter

app = FastAPI()

@app.get("/get_order/")
def get_order(id_order:int = None):
    request = {
        "body":{},
        "headers": {},
        "query_params": {
            "id_order": str(id_order)
        }
    }
    response = get_order_presenter(request, None)
    return response

@app.post("/create_order/")
def create_order(data: dict = None):
    event = {
        "body":data
    }
    
    response = create_order_presenter(event, None)
    return response