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
                table=1,
                id_order=0
                ),
            Order(
                hamburguer=Hamburguer(flavor=FLAVOR.CHICKEN),
                table=231231231,
                id_order=1
                ),
            Order(
                hamburguer=Hamburguer(flavor=FLAVOR.PORK),
                table=3,
                id_order=2
            ),
            Order(
                hamburguer=Hamburguer(flavor=FLAVOR.PORK),
                table=3,
                id_order=3
            )
        ]
        
    def create_order(self, table:int, flavor: FLAVOR) -> Order:
        order = Order(table=table, hamburguer=Hamburguer(flavor=flavor), id_order=len(self.orders))
        self.orders.append(order)
        
        return order
    
    def get_order(self, id_order: int) -> Order:
        for order in self.orders:
            if order.id_order == id_order:
                return order
            
        return None
