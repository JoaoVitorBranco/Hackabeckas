from src.shared.domain.repositories.hackabeckas_repository_interface import IHackabeckasRepository
from src.shared.domain.enums.flavor_enum import FLAVOR
from src.shared.domain.entities.order import Order

class CreateOrderUsecase:
    def __init__(self, repo: IHackabeckasRepository):
        self.repo = repo
    
    def __call__(self, table:int, flavor: FLAVOR) -> Order:
        return self.repo.create_order(table=table, flavor=flavor)
        


