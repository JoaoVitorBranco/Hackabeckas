from src.modules.get_order.get_order_viewmodel import GetOrderViewModel
from src.shared.infra.repositories.hackabeckas_repository_mock import HackabeckasRepositoryMock

class Test_GetOrderViewmodel:
    def test_get_order_viewmodel(self):
        repo = HackabeckasRepositoryMock()
        
        orderViewModel = GetOrderViewModel(order=repo.orders[0]).to_dict()
        
        assert orderViewModel == {'hamburguer': {'flavor': 'BEEF'}, 'table': 1, 'id_order': 0,'message': 'the order has been retrieved'}