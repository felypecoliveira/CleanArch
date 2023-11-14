from src.presentation.controllers.interface.controller_interface import ControllerInterface as Interface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.usecase.interfaces.contatos.select_contato_interface import InterfaceSelectContato


# id é do cliente
class SelectContatoController(Interface):
    def __init__(self, use_case: InterfaceSelectContato):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        id_cliente = http_request.body["id_"]
        response = self.__use_case.select_contato(id_cliente)

        return HttpResponse(
            status_code=200,
            body=response
        )
