from src.presentation.controllers.interface.controller import ControllerInterface as Interface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.interfaces.delete_contato import InterfaceDeleteContato


class DeleteContatoController(Interface):
    def __init__(self, use_case: InterfaceDeleteContato):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        delete_contato = http_request.body["id_"]
        response = self.__use_case.delete_contato(delete_contato)

        return HttpResponse(
            status_code=200,
            body=response
        )
