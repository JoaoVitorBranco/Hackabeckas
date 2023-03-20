from src.shared.helpers.http.http_fastapi_requests import FastAPIHttpRequest, FastAPIHttpResponse
from .get_order_usecase import GetOrderUsecase
from .get_order_controller import GetOrderController
from src.shared.infra.repositories.hackabeckas_repository_mock import HackabeckasRepositoryMock

def get_order_presenter(event, context):
    repo = HackabeckasRepositoryMock()
    usecase = GetOrderUsecase(repo)
    controller = GetOrderController(usecase)

    httpRequest = FastAPIHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = FastAPIHttpResponse(
        status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.to_dict()