from add_contato_cliente_validator import add_contato_cliente_validator


class MockRequest:
    def __init__(self) -> None:
        self.json = None


def test_add_contato_cliente_validator():
    print()

    requests = MockRequest()
    requests.json = {
        "id": 56,
        "nome_contato": "Andrerlei Camargo Silva",
        "telefone_contato": "62985582078",
        "email": "andrerlei_compras@sempre.com.br"

    }

    add_contato_cliente_validator(requests)


