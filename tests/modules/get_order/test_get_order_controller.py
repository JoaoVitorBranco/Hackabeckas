import pytest
from src.modules.get_order.get_order_controller import GetOrderController
from src.modules.get_order.get_order_usecase import GetOrderUsecase
from src.shared.infra.repositories.hackabeckas_repository_mock import HackabeckasRepositoryMock

from src.shared.helpers.http.http_models import HttpRequest

class Test_GetOrderController:
    def test_get_order_controller(self):
        repo = HackabeckasRepositoryMock()
        usecase = GetOrderUsecase(repo=repo)
        controller = GetOrderController(usecase=usecase)
        request = HttpRequest(
            query_params = {
                "id_order": "0"
            }
        )
        
        response = controller(request=request)
        
        assert response.status_code == 200
        assert response.body["hamburguer"]["flavor"] == "BEEF"
        assert response.body["table"] == 1
        assert response.body["message"] == "the order has been retrieved"
        
    def test_get_order_controller_id_order_is_missing(self):
        repo = HackabeckasRepositoryMock()
        usecase = GetOrderUsecase(repo=repo)
        controller = GetOrderController(usecase=usecase)
        request = HttpRequest(
            query_params = {
            }
        )
        
        response = controller(request=request)
        
        assert response.status_code == 400
        assert response.body == "Field id_order is missing"
        
    
    def test_get_order_controller_id_order_is_not_int(self):
        repo = HackabeckasRepositoryMock()
        usecase = GetOrderUsecase(repo=repo)
        controller = GetOrderController(usecase=usecase)
        request = HttpRequest(
            query_params = {
                "id_order": 1
            }
        )
        
        response = controller(request=request)
        
        assert response.status_code == 400
        assert response.body == "Field id_order is not valid"
    