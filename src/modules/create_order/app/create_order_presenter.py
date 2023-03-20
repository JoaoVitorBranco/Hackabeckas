from src.shared.helpers.http.http_fastapi_requests import FastAPIHttpRequest, FastAPIHttpResponse
from src.modules.create_order.app.create_order_usecase import CreateOrderUsecase
from src.modules.create_order.app.create_order_controller import CreateOrderController
from src.shared.infra.repositories.hackabeckas_repository_mock import HackabeckasRepositoryMock

def create_order_presenter(event, context):
    repo = HackabeckasRepositoryMock()
    usecase = CreateOrderUsecase(repo)
    controller = CreateOrderController(usecase)

    httpRequest = FastAPIHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = FastAPIHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.to_dict()
