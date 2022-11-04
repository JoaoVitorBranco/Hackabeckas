from abc import ABC, abstractmethod
from src.shared.domain.entities.order import Order
from src.shared.domain.enums.flavor_enum import FLAVOR


class IHackabeckasRepository(ABC):
    
    @abstractmethod
    def create_order(self, table:int, flavor: FLAVOR) -> Order:
        pass
   