from delete_cliente_validator import delete_cliente_validator


class MockRequest:
    def __init__(self) -> None:
        self.json = None


def test_delete_cliente_validator():
    print()
    request = MockRequest()
    request.json = {
        "id": 11
    }

    delete_cliente_validator(request)
