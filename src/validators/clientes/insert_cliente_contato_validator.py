from cerberus import Validator
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError


def insert_cliente_contato_validator(request: any):
    body_validator = Validator({
        "nome": {"type": "string", "required": True, "empty": False},
        "telefone": {"type": "string", "required": True, "empty": False},
        "cpf": {"type": "string", "required": True, "empty": False},
        "endereco": {"type": "string", "required": True, "empty": False},
        "data_nascimento": {"type": "string", "required": True, "empty": False},
        "nome_contato": {"type": "string", "required": True, "empty": False},
        "telefone_contato": {"type": "string", "required": True, "empty": False},
        "email": {"type": "string", "required": True, "empty": False}
    })

    response = body_validator.validate(request.json)

    if response is False:
        raise HttpUnprocessableEntityError(body_validator.errors)
