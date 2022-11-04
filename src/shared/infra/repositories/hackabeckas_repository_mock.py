from src.shared.domain.entities.order import Order
from src.shared.domain.entities.hamburguer import Hamburguer
from src.shared.domain.entities.order import Order
from src.shared.domain.repositories.hackabeckas_repository_interface import IHackabeckasRepository
from src.shared.domain.enums.flavor_enum import FLAVOR

class HackabeckasRepositoryMock(IHackabeckasRepository):
    orders: list[Order]
        
    def __init__(self):
        self.orders = [
            Order(
                hamburguer=Hamburguer(flavor=FLAVOR.BEEF),
                table=1
                ),
            Order(
                hamburguer=Hamburguer(flavor=FLAVOR.CHICKEN),
                table=231231231
                ),
            Order(
                hamburguer=Hamburguer(flavor=FLAVOR.PORK),
                table=3
            ),
            Order(
                hamburguer=Hamburguer(flavor=FLAVOR.PORK),
                table=3
            )
        ]
        
    def create_order(self, table:int, flavor: FLAVOR) -> Order:
        order = Order(table=table, hamburguer=Hamburguer(flavor=flavor))
        self.orders.append(Order(table=table, hamburguer=Hamburguer(flavor=flavor)))
        
        return order
    
