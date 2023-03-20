import json
from src.modules.create_order.app.create_order_presenter import create_order_presenter

class Test_CreateOrderPresenter:
    def test_create_order_presenter(self):
        event = {
            "body":{
                "flavor": "CHICKEN",
                "table": "1"
            }
        }
        
        expected = {
            "table": 1,
            "hamburguer":{
                "flavor": "CHICKEN"
            },
            "id_order": 4,
            
            "message": "the order has been created"
        }
        
        response = create_order_presenter(event, None)
        
        assert response["status_code"] == 201
        assert json.loads(response["body"]) == expected
        
    def test_create_order_presenter_missing_flavor(self):
        event = {
            "body":{
                "table": "1"
            }
        }
        

        expected = 'Field flavor is missing'
        
        response = create_order_presenter(event, None)
        
        assert response["status_code"] == 400
        assert response["body"] == json.dumps(expected)
        
        
    def test_create_order_presenter_table_must_be_decimal(self):
        event = {
            "body":{
                "flavor": "CHICKEN",
                "table": "string"
            }
        }
        

        expected = 'Field table is not valid'
        
        response = create_order_presenter(event, None)
        
        assert response["status_code"] == 400
        assert response["body"] == json.dumps(expected)
        