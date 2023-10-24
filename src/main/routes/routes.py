import json
from flask import Blueprint, request, jsonify

# Import adapters
from src.main.adapters.request_adapter import request_adapter

# Import composers clientes
from src.main.composer.clientes.delete_cliente import delete_cliente_composer
from src.main.composer.clientes.get_cliente_contatos import get_cliente_contatos_composer
from src.main.composer.clientes.get_clientes import get_clientes_composer
from src.main.composer.clientes.insert_cliente_contato import insert_cliente_contato_composer
from src.main.composer.clientes.update_cliente import update_cliente_composer

# Import composers contatos
from src.main.composer.contatos.update_contato import update_contato_composer
from src.main.composer.contatos.select_contato import select_contato_composer
from src.main.composer.contatos.get_contatos import get_contatos_composer
from src.main.composer.contatos.delete_contato import delete_contato_composer
from src.main.composer.contatos.addcontato_to_cliente import add_contato_to_cliente_composer

cliente_route_bp = Blueprint("clientes_routes", __name__)
contato_route_bp = Blueprint("contatos_routes", __name__)


# Clientes rotas
@cliente_route_bp.route("/cadastro", methods=["POST"])
def register_cliente_contato():
    http_response = request_adapter(request, insert_cliente_contato_composer())

    try:
        return jsonify(http_response.body), http_response.status_code
    except Exception:
        return {"mensagem": Exception}


@cliente_route_bp.route("/get/clientes", methods=["GET"])
def find_clientes():
    try:
        http_response = request_adapter(request, get_clientes_composer())
        return json.dumps({"body": str(http_response.body)})

    except Exception as e:
        return {"error": e}


@cliente_route_bp.route("/get/clientes_contatos", methods=["GET"])
def find_clientes_contatos():
    try:
        http_response = request_adapter(request, get_cliente_contatos_composer())
        return json.dumps({
            "body": str(http_response.body),
            "status_code": str(http_response.status_code)
        })

    except Exception as e:
        return {"error": e}


@cliente_route_bp.route("/delete/clientes", methods=["POST"])
def delete_cliente():
    http_response = request_adapter(request, delete_cliente_composer())

    try:
        if http_response:
            return json.dumps({"request": http_response.body})
    except Exception:
        return {"mensagem": Exception}


@cliente_route_bp.route("/update/clientes", methods=["POST"])
def update_cliente():
    http_response = request_adapter(request, update_cliente_composer())
    body_lista = http_response.body
    try:
        if http_response:
            return json.dumps({
                "body": str(body_lista),
                "status_code": str(http_response.status_code)
            })


    except Exception as e:
        return {"error": e}


# Contatos rotas
@contato_route_bp.route("/get/contatos", methods=["GET"])
def get_contatos():
    try:
        http_response = request_adapter(request, get_contatos_composer())
        return json.dumps({
            "body": str(http_response.body),
            "status_code": str(http_response.status_code)
        })

    except Exception as e:
        return {"error": e}


@contato_route_bp.route("/select/contato", methods=["GET"])
def select_contatos():
    http_response = request_adapter(request, select_contato_composer())
    body_lista = http_response.body
    try:
        if http_response:
            return json.dumps({
                "body": str(body_lista),
                "status_code": str(http_response.status_code)
            })


    except Exception as e:
        return {"error": e}


@contato_route_bp.route("/update/contato", methods=["POST"])
def update_contatos():
    http_response = request_adapter(request, update_contato_composer())
    body_lista = http_response.body
    try:
        if http_response:
            return json.dumps({
                "body": str(body_lista),
                "status_code": str(http_response.status_code)
            })




    except Exception as e:
        return {"error": e}
