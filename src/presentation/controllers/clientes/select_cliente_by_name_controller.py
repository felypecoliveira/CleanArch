from src.presentation.controllers.interface.controller_interface import ControllerInterface as Interface
from src.usecase.interfaces.clientes.select_cliente_by_name_interface import InterfaceSelectClienteByName
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.http_types.http_request import HttpRequest


class SelectClienteByNameController(Interface):
    def __init__(self, use_case: InterfaceSelectClienteByName):
        self.use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        nome = http_request.body["nome"]

        response = self.use_case.select_cliente_by_name(nome)

        if response is None:
            return HttpResponse(
                status_code=404,
                body={"response": "cliente not found", "status_code": 404}
            )

        return HttpResponse(
            status_code=200,
            body={"data": response}
        )
