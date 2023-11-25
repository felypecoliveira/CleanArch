from src.presentation.controllers.contatos.delete_contato_controller import DeleteContatoController
from src.infra.tests.contato_repository import ContatosRepositorySpy
from src.presentation.http_types.http_response import HttpResponse


class HttpResquetMock:
    def __init__(self):
        self.body = {"id_": 22}



def test_handle():
    htt_request_mock = HttpResquetMock()
    use_case = ContatosRepositorySpy()
    controller = DeleteContatoController(use_case)

    response = controller.handle(htt_request_mock)

    assert isinstance(response, HttpResponse)
