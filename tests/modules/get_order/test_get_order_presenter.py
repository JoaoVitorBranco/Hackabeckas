import json
from src.modules.get_order.get_order_presenter import get_order_presenter
import pytest

class Test_GetOrderPresenter:
    def test_get_order_presenter(self):
        event = {
            "headers": {
                "header1": "value1",
                "header2": "value1,value2"
            },
            "body": {},
            "query_params":{"id_order":"0"}
        }
        
        expected = {'hamburguer': {'flavor': 'BEEF'}, 'table': 1, 'id_order': 0,'message': 'the order has been retrieved'}
        
        response = get_order_presenter(event, None)
        
        assert json.loads(response["body"]) == expected
        assert response["status_code"] == 200
        
    def test_get_order_presenter_not_found(self):
        event = {
            "headers": {
                "header1": "value1",
                "header2": "value1,value2"
            },
            "body": {},
            "query_params":{"id_order":"4"}
        }
        
        
        response = get_order_presenter(event, None)
        
        assert response["status_code"] == 404
        assert response["message"] == "the order has not been found"