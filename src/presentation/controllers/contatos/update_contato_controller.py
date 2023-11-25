from src.presentation.controllers.interface.controller_interface import ControllerInterface as Interface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.usecase.interfaces.contatos.update_contato_interface import InterfaceUpdateContatos


class UpdateContatoController(Interface):
    def __init__(self, use_case: InterfaceUpdateContatos):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        id_contatos = http_request.body["id_contatos"]
        column = http_request.body["column"]
        update_ = http_request.body["update_"]
        response = self.__use_case.update_contato(id_contatos, column, update_)

        return HttpResponse(
            status_code=200,
            body={"data": response}
        )
