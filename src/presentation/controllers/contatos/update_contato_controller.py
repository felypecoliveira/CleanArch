from src.presentation.controllers.interface.controller import ControllerInterface as Interface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.interfaces.update_contato import InterfaceUpdateContatos


class UpdateContatoController(Interface):
    def __init__(self, use_case: InterfaceUpdateContatos):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        update_contato = http_request.query_params[["id_", "column", "update_"]]
        response = self.__use_case.update_contato(**update_contato)

        return HttpResponse(
            status_code=200,
            body=response
        )
