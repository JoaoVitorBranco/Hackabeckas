from src.shared.helpers.http.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from src.modules.create_order.app.create_order_usecase import CreateOrderUsecase
from src.modules.create_order.app.create_order_controller import CreateOrderController
from src.shared.infra.repositories.hackabeckas_repository_mock import HackabeckasRepositoryMock

def lambda_handler(event, context):
    repo = HackabeckasRepositoryMock()
    usecase = CreateOrderUsecase(repo)
    controller = CreateOrderController(usecase)

    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()
