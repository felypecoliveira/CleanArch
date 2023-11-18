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
    try:
        # Inserir contato para um cliente especifico
        mock_id_cliente = 106
        mock_nome_contato = fake.name()
        mock_telefone_contato = __random_phone_numbers()
        mock_email = fake.email()
        repository.add_contato_to_cliente(mock_id_cliente,
                                          mock_nome_contato,
                                          mock_telefone_contato,
                                          mock_email)

        stmt = f"""
        SELECT * FROM CONTATOS
        WHERE NOME_CONTATO = '{mock_nome_contato}'
        AND TELEFONE_CONTATO = '{mock_telefone_contato}'
        AND EMAIL = '{mock_email}'
        """

        response = connection.execute(text(stmt))
        registry = response.fetchall()[0]
        assert registry.nome_contato == mock_nome_contato
        assert registry.telefone_contato == mock_telefone_contato
        assert registry.email == mock_email

        __deletion(registry)

    except:
        __deletion(registry)


def test_delete_contato():
    try:
        mock_id_contato = 159
        repository.delete_contato(mock_id_contato)

        stmt = f"""
        SELECT * FROM CONTATOS
        WHERE ID_CONTATOS = {mock_id_contato}
        """

        response = connection.execute(text(stmt))
        registry = response.fetchone()

        assert registry is None

    except:
        __deletion(registry)


def test_select_contato():
    # digite o id do contato para a query
    mock_id_cliente = 106
    repository.select_contato(mock_id_cliente)

    stmt = f"""
    SELECT * FROM CONTATOS
    WHERE id_cliente = {mock_id_cliente}
    """

    response = connection.execute(text(stmt))
    registry = response.fetchone()

    print(registry)

    assert registry.id_cliente == mock_id_cliente
    ...


def test_update_contato():
    mock_id_contato = 228
    mock_column = "nome_contato"
    mock_update = "Pietra Diniz Alvez"

    repository.update_contato(mock_id_contato,
                              mock_column,
                              mock_update)

    stmt = f"""
        SELECT * FROM CONTATOS
        WHERE ID_CONTATOS = {mock_id_contato}
        """

    response = connection.execute(text(stmt))
    registry = response.fetchall()

    print(registry)

    assert registry.nome_contato == mock_update

  
def __random_phone_numbers():
    prefixos = ["62", "66"]
    prefixo = random.choice(prefixos)
    resto_n = random.randint(10000000, 99999999)
    return f'{prefixo}{resto_n}'


def __deletion(registry):
    connection.execute(text(f"DELETE FROM CONTATOS "
                            f"WHERE ID_CONTATOS = {registry.id_contatos}"))
    connection.commit()
