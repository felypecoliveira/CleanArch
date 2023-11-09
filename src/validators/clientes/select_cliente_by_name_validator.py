from cerberus import Validator
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError


def select_cliente_by_name_validator(request: any):
    query_validator = Validator({
        "nome": {"type": "string", "required": True, "empty": False}
    })

    response = query_validator.validate(request.json)

    if response is False:
        raise HttpUnprocessableEntityError(query_validator.errors)
