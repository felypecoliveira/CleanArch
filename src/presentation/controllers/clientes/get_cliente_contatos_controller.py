from src.presentation.controllers.interface.controller_interface import ControllerInterface as Interface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.usecase.interfaces.clientes.get_clientes_contatos_interface import InterfaceGetClientesContatos


class GetClientesContatosController(Interface):
    def __init__(self, use_case: InterfaceGetClientesContatos):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        response = self.__use_case.get_clientes_contatos()

        return HttpResponse(
            status_code=200,
            body=response
        )

