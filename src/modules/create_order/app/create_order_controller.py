from src.modules.create_order.app.create_order_viewmodel import CreateOrderViewModel
from src.modules.create_order.app.create_order_usecase import CreateOrderUsecase
from src.shared.helpers.http.http_models import BadRequest, Created, HttpRequest, HttpResponse, InternalServerError
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.domain.enums.flavor_enum import FLAVOR

class CreateOrderController:
    def __init__(self, usecase: CreateOrderUsecase):
        self.createOrderUsecase = usecase
        
    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            if request.body.get('table') is None:
                raise MissingParameters('table')
                
            if request.body.get('flavor') is None:
                raise MissingParameters('flavor')
            
            if not request.body["table"].isdecimal():
                raise EntityError("table")

            flavors = list()
            for flavor in FLAVOR:
                flavors.append(flavor.value)
                
            if request.body["flavor"] not in flavors:
                raise EntityError("flavor")

            order = self.createOrderUsecase(flavor=FLAVOR[request.body["flavor"]], table=int(request.body["table"]))
            viewmodel = CreateOrderViewModel(order=order)
            
            return Created(viewmodel.to_dict())
            
        except EntityError as err:
            return BadRequest(body=err.message)
            
        except MissingParameters as err:
            return BadRequest(body=err.message)    
            
        except Exception as err:
            return InternalServerError(body=err.args[0])


