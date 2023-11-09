from cerberus import Validator
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError


def update_cliente_validator(request: any):
    body_validator = Validator({
        "id_": {"type": "integer", "required": True, "empty": False},
        "column": {"type": "string", "required": True, "empty": False},
        "update_": {"type": "string", "required": True, "empty": False}
    })

    response = body_validator.validate(request.json)

    if response is False:
        raise HttpUnprocessableEntityError(body_validator.errors)
