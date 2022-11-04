from src.shared.domain.entities.order import Order
from src.shared.domain.entities.hamburguer import Hamburguer
from src.shared.domain.enums.flavor_enum import FLAVOR


class HamburguerViewModel:
    hamburguer: Hamburguer
    
    def __init__(self, hamburguer:Hamburguer):
        self.hamburguer = hamburguer
        
    def to_dict(self) -> dict:
        return {
            "flavor": self.hamburguer.flavor.value
        }
        
class CreateOrderViewModel:
    order: Order
    
    def __init__(self, order:Order):
        self.order = order
        
    def to_dict(self) -> dict:
        return {
            "table": self.order.table,
            "hamburguer": HamburguerViewModel(self.order.hamburguer).to_dict()
        }