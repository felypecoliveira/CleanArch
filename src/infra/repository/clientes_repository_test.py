from src.infra.db.connect_settings import ConnectionHandler
from clientes_repository import ClientesRepository

db_connection_handler = ConnectionHandler()
connection = db_connection_handler.get_engine().connect()


def test_update_cliente():
    clientes_repositorys = ClientesRepository()


def select_cliente_by_name():
    clientes_repositorys = ClientesRepository()


def test_insert_cliente_contato():
    clientes_repositorys = ClientesRepository()


def get_clientes():
    clientes_repositorys = ClientesRepository()


def get_clientes_contatos():
    clientes_repositorys = ClientesRepository()


def delete_cliente():
    clientes_repositorys = ClientesRepository()
