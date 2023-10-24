from src.presentation.controllers.interface.controller import ControllerInterface as Interface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.interfaces.update_cliente import InterfaceUpdateCliente


class UpdateClientesController(Interface):
    def __init__(self, use_case: InterfaceUpdateCliente):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        id_ = http_request.body["id_"]
        column = http_request.body["column"]
        update_ = http_request.body["update_"]
        response = self.__use_case.update_cliente(id_, column, update_)

        return HttpResponse(
            status_code=200,
            body=response

        )
