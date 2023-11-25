from insert_cliente_contato_validator import insert_cliente_contato_validator


class MockRequest:
    def __init__(self) -> None:
        self.json = None


def test_insert_cliente_contato_validator():
    print()
    request = MockRequest()
    request.json = {

        "nome": "Andre Felype Camargo Oliveira",
        "telefone": "62985785227",
        "cpf": "05110918180",
        "endereco": "Av tocantis Sampaio 1098, GO",
        "data_nascimento": "1998-08-15",
        "nome_contato": "Lucas Bitencourt",
        "telefone_contato": "62992717962",
        "email": "lcastilho@rgnarok.com"

    }

    insert_cliente_contato_validator(request)
