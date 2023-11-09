from src.infra.db.connect_settings import ConnectionHandler
from contatos_repository import ContatosRepository

db_connection_handler = ConnectionHandler()
connection = db_connection_handler.get_engine().connect()


def test_add_contato_to_cliente():
    contatos_repository = ContatosRepository()


def test_delete_contato():
    contatos_repository = ContatosRepository()


def test_get_contatos():
    contatos_repository = ContatosRepository()


def test_select_contato():
    contatos_repository = ContatosRepository()


def test_update_contato():
    contatos_repository = ContatosRepository()


