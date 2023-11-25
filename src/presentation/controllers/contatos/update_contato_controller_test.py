from src.infra.tests.contato_repository import ContatosRepositorySpy
from src.presentation.controllers.contatos.update_contato_controller import UpdateContatoController
from src.presentation.http_types.http_response import HttpResponse


class HttpResquetMock:
    def __init__(self):
        self.body = {"id_contatos": 33,
                     "column": "nome_contato",
                     "update_": "Jessica Farias"}






def test_handle():
    htt_request_mock = HttpResquetMock()
    use_case = ContatosRepositorySpy()
    controller = UpdateContatoController(use_case)

    response = controller.handle(htt_request_mock)

    print(response.body["data"])


    assert isinstance(response, HttpResponse)