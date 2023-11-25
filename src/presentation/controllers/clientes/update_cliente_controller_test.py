from src.presentation.controllers.clientes.update_cliente_controller import UpdateClientesController

from src.infra.tests.cliente_repository import ClientesRespositorySpy
from src.presentation.http_types.http_response import HttpResponse


class HttpResquetMock:
    def __init__(self):
        self.body = {"id_": 23, "column": "nome", "update_": "Joao Mendrado"}


def test_handle():
    htt_request_mock = HttpResquetMock()
    use_case = ClientesRespositorySpy()
    controller = UpdateClientesController(use_case)

    response = controller.handle(htt_request_mock)
    print(response.body["data"])

    assert isinstance(response, HttpResponse)
