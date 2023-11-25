from src.presentation.controllers.interface.controller_interface import ControllerInterface as Interface
from src.usecase.interfaces.clientes.insert_cliente_contato_interface import InterfaceClienteContato
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.http_types.http_request import HttpRequest


class InsertClientesContatosController(Interface):
    def __init__(self, use_case: InterfaceClienteContato):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        nome = http_request.body["nome"]
        telefone = http_request.body["telefone"]
        cpf = http_request.body["cpf"]
        endereco = http_request.body["endereco"]
        data_nascimento = http_request.body["data_nascimento"]
        nome_contato = http_request.body["nome_contato"]
        telefone_contato = http_request.body["telefone_contato"]
        email = http_request.body["email"]

        response = self.__use_case.insert_cliente_contato(nome,
                                                          telefone,
                                                          cpf,
                                                          endereco,
                                                          data_nascimento,
                                                          nome_contato,
                                                          telefone_contato,
                                                          email)

        return HttpResponse(
            status_code=200,
            body={"data": response}
        )
