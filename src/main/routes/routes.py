import json
from flask import Blueprint, request, jsonify

# Import adapters
from src.main.adapters.request_adapter import request_adapter

# Import composers clientes
from src.main.composer.clientes.select_cliente_by_name_composer import select_cliente_by_name_composer
from src.main.composer.clientes.insert_cliente_contato_composer import insert_cliente_contato_composer
from src.main.composer.clientes.get_cliente_contatos_composer import get_cliente_contatos_composer
from src.main.composer.clientes.delete_cliente_composer import delete_cliente_composer
from src.main.composer.clientes.update_cliente_composer import update_cliente_composer
from src.main.composer.clientes.get_clientes_composer import get_clientes_composer

# Import composers contatos
from src.main.composer.contatos.addcontato_to_cliente_composer import add_contato_to_cliente_composer
from src.main.composer.contatos.delete_contato_composer import delete_contato_composer
from src.main.composer.contatos.update_contato_composer import update_contato_composer
from src.main.composer.contatos.select_contato_composer import select_contato_composer
from src.main.composer.contatos.get_contatos_composer import get_contatos_composer

# Import handle errors
from src.errors.error_handler import handle_errors

# Import validators clientes
from src.validators.clientes.insert_cliente_contato_validator import insert_cliente_contato_validator
from src.validators.clientes.update_cliente_validator import update_cliente_validator
from src.validators.clientes.select_cliente_by_name_validator import select_cliente_by_name_validator
from src.validators.clientes.delete_cliente_validator import delete_cliente_validator

# Import validators contatos
from src.validators.contatos.add_contato_cliente_validator import add_contato_cliente_validator
from src.validators.contatos.delete_contato_validator import delete_contato_validator
from src.validators.contatos.select_contato_validator import select_contato_validator
from src.validators.contatos.update_contato_validator import update_contato_validator

# Nomeando rotas
cliente_route_bp = Blueprint("clientes_routes", __name__)
contato_route_bp = Blueprint("contatos_routes", __name__)


# Clientes rotas
@cliente_route_bp.route("/cadastro", methods=["POST"])
def register_cliente_contato():
    http_response = None
    try:
        insert_cliente_contato_validator(request)
        http_response = request_adapter(request, insert_cliente_contato_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(str(http_response.body)), str(http_response.status_code)


@cliente_route_bp.route("/get/clientes", methods=["GET"])
def find_clientes():
    http_response = None
    try:
        http_response = request_adapter(request, get_clientes_composer())
        if http_response:
            return json.dumps(
                {"body": str(http_response.body),
                 "status": str(http_response.status_code)
                 })

    except Exception as exception:
        http_response = handle_errors(exception)
        return {"error": http_response}


@cliente_route_bp.route("/get/clientes_contatos", methods=["GET"])
def find_clientes_contatos():
    http_response = None
    try:
        http_response = request_adapter(request, get_cliente_contatos_composer())

    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(str(http_response.body)), str(http_response.status_code)


@cliente_route_bp.route("/select/by_name/cliente", methods=["GET"])
def select_cliente_by_names():
    http_response = None
    try:
        select_cliente_by_name_validator(request)
        http_response = request_adapter(request, select_cliente_by_name_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(str(http_response.body)), str(http_response.status_code)


@cliente_route_bp.route("/delete/clientes", methods=["POST"])
def delete_cliente():
    http_response = None
    try:
        delete_cliente_validator(request)
        http_response = request_adapter(request, delete_cliente_composer())

    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(str(http_response.body)), str(http_response.status_code)


@cliente_route_bp.route("/update/clientes", methods=["POST"])
def update_cliente():
    http_response = None
    try:
        update_cliente_validator(request)
        http_response = request_adapter(request, update_cliente_composer())

    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(str(http_response.body)), str(http_response.status_code)


# Contatos rotas
@contato_route_bp.route("/get/contatos", methods=["GET"])
def get_contatos():
    http_response = None
    try:
        http_response = request_adapter(request, get_contatos_composer())

    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(str(http_response.body)), str(http_response.status_code)


# Numero do cliente necessario para selecionar respectivos contatos
@contato_route_bp.route("/select/contatos", methods=["GET"])
def select_contatos():
    http_response = None
    try:
        select_contato_validator(request)
        http_response = request_adapter(request, select_contato_composer())

    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(str(http_response.body)), str(http_response.status_code)


@contato_route_bp.route("/update/contatos", methods=["POST"])
def update_contatos():
    http_response = None
    try:
        update_contato_validator(request)
        http_response = request_adapter(request, update_contato_composer())

    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(str(http_response.body)), str(http_response.status_code)


@contato_route_bp.route("/delete/contatos", methods=["POST"])
def delete_contato():
    http_response = None
    try:
        delete_contato_validator(request)
        http_response = request_adapter(request, delete_contato_composer())

    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(str(http_response.body)), str(http_response.status_code)


@contato_route_bp.route("/add/contatos", methods=["POST"])
def add_contato_to_cliente():
    http_response = None
    try:
        add_contato_cliente_validator(request)
        http_response = request_adapter(request, add_contato_to_cliente_composer())

    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(str(http_response.body)), str(http_response.status_code)
