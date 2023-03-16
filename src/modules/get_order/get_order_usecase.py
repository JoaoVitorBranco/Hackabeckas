from shared.domain.entities.order import Order
from shared.domain.repositories.hackabeckas_repository_interface import IHackabeckasRepository


class GetOrderUsecase:
    def __init__(self, repo: IHackabeckasRepository):
        self.repo = repo

    def get_order(self, order_id: str) -> Order:
        return self.repo.get_order(order_id)