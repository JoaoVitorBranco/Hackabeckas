from src.modules.create_order.app.create_order_viewmodel import CreateOrderViewModel
from src.shared.infra.repositories.hackabeckas_repository_mock import HackabeckasRepositoryMock

class Test_CreateOrderViewModel:
    def test_create_order_viewmodel(self):
        repo = HackabeckasRepositoryMock()
        
        orderViewModel = CreateOrderViewModel(order=repo.orders[0]).to_dict()
        
        assert orderViewModel == {'hamburguer': {'flavor': 'BEEF'}, 'table': 1, 'message': 'the order has been created'}