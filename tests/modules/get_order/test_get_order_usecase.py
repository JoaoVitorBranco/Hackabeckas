from src.modules.get_order.get_order_usecase import GetOrderUsecase
from src.shared.domain.enums.flavor_enum import FLAVOR
from src.shared.infra.repositories.hackabeckas_repository_mock import HackabeckasRepositoryMock
import pytest

class Test_GetOrderUsecase:
    def test_get_order_usecase(self):
        repo = HackabeckasRepositoryMock()
        usecase = GetOrderUsecase(repo=repo)
        
        order = usecase(id_order=0)
        
        assert order.table == 1
        assert order.hamburguer.flavor == FLAVOR.BEEF 
        assert order.id_order == 0