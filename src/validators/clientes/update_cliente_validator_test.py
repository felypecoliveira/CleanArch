from update_cliente_validator import update_cliente_validator


class MockRequest:
    def __init__(self) -> None:
        self.json = None


def test_update_cliente_validator():
    print()
    requests = MockRequest()

    requests.json = {

        "id_": 12,
        "column": "nome",
        "update_": "Felype Figueiredo"
    }

    update_cliente_validator(requests)



