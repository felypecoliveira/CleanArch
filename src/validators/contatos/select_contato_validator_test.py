from select_contato_validator import select_contato_validator


class MockRequest:
    def __init__(self) -> None:
        self.json = None



def test_select_contato_validator():
    print()

    requests = MockRequest()
    requests.json = {
        "id_": 23
    }

    select_contato_validator(requests)