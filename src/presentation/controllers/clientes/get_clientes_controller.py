from src.presentation.controllers.interface.controller import ControllerInterface as Interface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.interfaces.get_clientes import InterfaceGetCliente


class GetClientesController(Interface):
    def __init__(self, use_case: InterfaceGetCliente):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        response = self.__use_case.get_clientes()

        return HttpResponse(
            status_code=200,
            body=response
        )

