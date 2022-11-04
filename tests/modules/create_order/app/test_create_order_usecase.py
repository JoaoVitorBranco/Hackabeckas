import pytest
from src.shared.domain.repositories.hackabeckas_repository_interface import IHackabeckasRepository
from src.shared.domain.enums.flavor_enum import FLAVOR
from src.shared.domain.entities.order import Order
from src.shared.infra.repositories.hackabeckas_repository_mock import HackabeckasRepositoryMock
from src.modules.create_order.app.create_order_usecase import CreateOrderUsecase



class Test_CreateOrderUsecase:
    def test_create_order_usecase(self):
        repo = HackabeckasRepositoryMock()
        usecase = CreateOrderUsecase(repo=repo)
        
        lenBefore = len(repo.orders)
        
        order = usecase(table=4, flavor=FLAVOR.CHICKEN)
        
        assert len(repo.orders) == lenBefore + 1
        assert order.table == 4
        assert order.hamburguer.flavor == FLAVOR.CHICKEN 
        


