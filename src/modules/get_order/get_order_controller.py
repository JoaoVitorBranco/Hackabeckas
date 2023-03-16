from src.shared.helpers.errors.usecase_errors import NoItemsFound
from .get_order_usecase import GetOrderUsecase
from .get_order_viewmodel import GetOrderViewModel
from src.shared.helpers.http.http_models import BadRequest, OK, HttpRequest, HttpResponse, InternalServerError, NotFound
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.domain.enums.flavor_enum import FLAVOR

class GetOrderController:
    def __init__(self, usecase: GetOrderUsecase):
        self.getOrderUsecase = usecase
        
    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            if request.query_params.get('id_order') is None:
                raise MissingParameters('id_order')
                
            if type(request.query_params.get('id_order')) != str:
                raise EntityError('id_order')
            
            if not request.query_params["id_order"].isdecimal():
                raise EntityError("id_order")

            order = self.getOrderUsecase(id_order=int(request.query_params["id_order"]))
            viewmodel = GetOrderViewModel(order=order)
            
            return OK(viewmodel.to_dict())
            
        except EntityError as err:
            return BadRequest(body=err.message)
        
        except NoItemsFound as err:
            return NotFound(body=err.message)
            
        except MissingParameters as err:
            return BadRequest(body=err.message)    
            
        except Exception as err:
            return InternalServerError(body=err.args[0])


