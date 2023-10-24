from src.presentation.controllers.interface.controller import ControllerInterface as Interface
from src.interfaces.addcontato_to_cliente import InterfaceContatoCliente
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.http_types.http_request import HttpRequest


class AddContatoController(Interface):
    def __init__(self, use_case: InterfaceContatoCliente):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        add_contato = http_request.query_params["id", "nome_contato", "telefone", "email"]

        response = self.__use_case.add_contato_to_cliente(**add_contato)

        return HttpResponse(
            status_code=200,
            body=response
        )
