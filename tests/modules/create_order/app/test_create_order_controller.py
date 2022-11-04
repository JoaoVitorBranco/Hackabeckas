import pytest
from src.shared.infra.repositories.hackabeckas_repository_mock import HackabeckasRepositoryMock
from src.modules.create_order.app.create_order_usecase import CreateOrderUsecase
from src.modules.create_order.app.create_order_controller import CreateOrderController
from src.shared.helpers.http.http_models import HttpRequest

class Test_CreateOrderController:
    def test_create_order_controller(self):
        repo = HackabeckasRepositoryMock()
        usecase = CreateOrderUsecase(repo=repo)
        controller = CreateOrderController(usecase=usecase)
        request = HttpRequest(
            body = {
                "flavor": "CHICKEN",
                "table": "12"
            }
        )
        
        response = controller(request=request)
        
        assert response.status_code == 201
        assert response.body["hamburguer"]["flavor"] == "CHICKEN"
        assert response.body["table"] == 12
        assert response.body["message"] == "the order has been created"
        
    def test_create_order_controller_table_is_missing(self):
        repo = HackabeckasRepositoryMock()
        usecase = CreateOrderUsecase(repo=repo)
        controller = CreateOrderController(usecase=usecase)
        request = HttpRequest(
            body = {
                "flavor": "CHICKEN"
            }
        )
        
        response = controller(request=request)
        
        assert response.status_code == 400
        assert response.body == "Field table is missing"
        
    def test_create_order_controller_table_not_decimal(self):
        repo = HackabeckasRepositoryMock()
        usecase = CreateOrderUsecase(repo=repo)
        controller = CreateOrderController(usecase=usecase)
        request = HttpRequest(
            body = {
                "flavor": "CHICKEN",
                "table": "OutroQualquerCoisa"
            }
        )
        
        response = controller(request=request)
        
        assert response.status_code == 400
        assert response.body == "Field table is not valid"
    
    def test_create_order_controller_flavor_not_enum(self):
        repo = HackabeckasRepositoryMock()
        usecase = CreateOrderUsecase(repo=repo)
        controller = CreateOrderController(usecase=usecase)
        request = HttpRequest(
            body = {
                "flavor": "QualquerCoisa",
                "table": "1"
            }
        )
        
        response = controller(request=request)
        
        assert response.status_code == 400
        assert response.body == "Field flavor is not valid"
    