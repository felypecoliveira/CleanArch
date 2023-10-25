from src.presentation.controllers.interface.controller import ControllerInterface as Interface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.interfaces.clientes.delete_cliente import InterfaceDeleteCliente


class DeleteClienteController(Interface):
    def __init__(self, use_case: InterfaceDeleteCliente):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        deletion = http_request.body['id']
        response = self.__use_case.delete_cliente(deletion)

        return HttpResponse(
            status_code=200,
            body=response
        )

