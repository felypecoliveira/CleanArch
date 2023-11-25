from src.presentation.controllers.clientes.delete_cliente_controller import DeleteClienteController
from src.infra.tests.cliente_repository import ClientesRespositorySpy
from src.presentation.http_types.http_response import HttpResponse



class HttpResquetMock:
    def __init__(self) -> None:
        self.body = {"id": 23}


def test_handle():
    http_request_mock = HttpResquetMock()
    use_case = ClientesRespositorySpy()
    controller = DeleteClienteController(use_case)

    response = controller.handle(http_request_mock)
    assert isinstance(response, HttpResponse)
