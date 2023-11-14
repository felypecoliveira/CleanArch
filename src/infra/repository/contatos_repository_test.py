from src.infra.db.connect_settings import ConnectionHandler
from contatos_repository import ContatosRepository
from sqlalchemy import text
from faker import Faker
import random


db_connection_handler = ConnectionHandler()
connection = db_connection_handler.get_engine().connect()
repository = ContatosRepository()
fake = Faker("pt_BR")

def test_add_contato_to_cliente():
    # Inserir contato para um cliente especifico
    mock_nome_contato = fake.nome
    mock
    ...


def test_delete_contato():
    ...


def test_get_contatos():
    ...


def test_select_contato():
    ...


def test_update_contato():
    ...


