from src.presentation.controllers.clientes.select_cliente_by_name_controller import SelectClienteByNameController
from src.infra.tests.cliente_repository import ClientesRespositorySpy
from src.presentation.http_types.http_response import HttpResponse


class HttpResquetMock:
    def __init__(self):
        self.body = {"nome": "Meu Nome"}


def test_handle():
    htt_request_mock = HttpResquetMock()
    use_case = ClientesRespositorySpy()
    controller = SelectClienteByNameController(use_case)

    response = controller.handle(htt_request_mock)
    print(response.body["data"])

    assert isinstance(response, HttpResponse)