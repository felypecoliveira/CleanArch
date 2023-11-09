from cerberus import Validator
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError


def add_contato_cliente_validator(request: any):
    body_validator = Validator({
        "id": {"type": "integer", "required": True, "empty": False},
        "nome_contato":{"type":"string", "required": True, "empty":False},
        "telefone_contato":{"type":"string", "required": True, "empty":False},
        "email":{"type":"string", "required": True, "empty":False},
    })

    response = body_validator.validate(request.json)

    if response is False:
        raise HttpUnprocessableEntityError(body_validator.errors)
