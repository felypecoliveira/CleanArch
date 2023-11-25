from update_contato_validator import update_contato_validator


class MockRequest:
    def __init__(self) -> None:
        self.json = None


def test_update_contato_validator():
    print()

    requests = MockRequest()
    requests.json = {
        "id_contatos": 44,
        "column": "nome_contato",
        "update_": "Alexandra Menezes Costa"
    }

    update_contato_validator(requests)


