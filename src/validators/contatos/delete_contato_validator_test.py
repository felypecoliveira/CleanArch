from delete_contato_validator import delete_contato_validator


class MockRequest:
    def __init__(self) -> None:
        self.json = None


def test_delete_contato_validator():
    print()

    requests = MockRequest()
    requests.json = {"id_contatos": 123}

    delete_contato_validator(requests)

