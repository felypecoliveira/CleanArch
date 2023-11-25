from src.infra.tests.contato_repository import ContatosRepositorySpy
from select_contato_controller import SelectContatoController
from src.presentation.http_types.http_response import HttpResponse


class HttpResquetMock:
    def __init__(self):
        self.body = {"id_": 23}



def test_handle():
    htt_request_mock = HttpResquetMock()
    use_case = ContatosRepositorySpy()
    controller = SelectContatoController(use_case)

    response = controller.handle(htt_request_mock)

    print(response.body["data"])


    assert isinstance(response, HttpResponse)

