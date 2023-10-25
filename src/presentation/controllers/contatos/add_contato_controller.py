from src.presentation.controllers.interface.controller import ControllerInterface as Interface
from src.interfaces.contatos.addcontato_to_cliente import InterfaceContatoCliente
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.http_types.http_request import HttpRequest


class AddContatoController(Interface):
    def __init__(self, use_case: InterfaceContatoCliente):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        try:
            id_cliente = http_request.body["id"]
            nome_contato = http_request.body["nome_contato"]
            telefone_contato = http_request.body["telefone_contato"]
            email = http_request.body["email"]

            response = self.__use_case.add_contato_to_cliente(id_cliente,
                                                              nome_contato,
                                                              telefone_contato,email)

            return HttpResponse(
                status_code=200,
                body=response
            )

        except Exception as exception:
            return {"error": exception}