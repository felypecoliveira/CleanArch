from select_cliente_by_name_validator import select_cliente_by_name_validator


class MockRequest:
    def __init__(self) -> None:
        self.json = None


def test_select_cliente_by_name_validator():
    print()
    request = MockRequest()

    request.json = {
        "nome": "Andre Felype Camargo Oliveira"
    }

    select_cliente_by_name_validator(request)
