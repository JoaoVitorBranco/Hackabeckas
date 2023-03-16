class GetOrderUsecase():
    def __init__(self, repo):
        self.repo = repo
    def __call__(self, id_order:int):
        return self.repo.get_order(id_order=id_order)