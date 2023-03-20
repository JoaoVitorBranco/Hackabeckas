from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class GetOrderUsecase():
    def __init__(self, repo):
        self.repo = repo
    def __call__(self, id_order:int):
        if id_order < 0:
            raise EntityError("id_order")
        order = self.repo.get_order(id_order=id_order)
        
        if order is None:
            raise NoItemsFound("id_order")
        
        return self.repo.get_order(id_order=id_order)