from src.infra.db.connect_settings import ConnectionHandler
from clientes_repository import ClientesRepository
from sqlalchemy import text
from faker import Faker
import random

clientes_repositorys = ClientesRepository()
db_connection_handler = ConnectionHandler()
connection = db_connection_handler.get_engine().connect()
fake = Faker("pt_BR")


def random_phone_numbers():
    prefixos = ["62", "66"]
    prefixo = random.choice(prefixos)
    resto_n = random.randint(10000000, 99999999)
    return f'{prefixo}{resto_n}'


def teste_delete_cliente():
    ...


def test_update_cliente():
    try:
        # Clientes atributos
        mocked_update_nome = fake.name()
        mocked_update_telefone = random_phone_numbers()
        mocked_update_cpf = fake.cpf()
        mocked_update_endereco = fake.address()
        mocked_update_data_nascimento = fake.date_of_birth(minimum_age=20, maximum_age=85)

        # Contatos atributos
        mocked_update_contato_nome = fake.name()
        mocked_update_telefone_contato = random_phone_numbers()
        mocked_update_email = fake.email()

        # Inserindo clientes e contatos
        clientes_repositorys.insert_cliente_contato(
            mocked_update_nome,
            mocked_update_telefone,
            mocked_update_cpf,
            mocked_update_endereco,
            mocked_update_data_nascimento,
            mocked_update_contato_nome,
            mocked_update_telefone_contato,
            mocked_update_email
        )

        sql = f"""
        SELECT * FROM CLIENTES
        WHERE NOME = '{mocked_update_nome}'
        AND TELEFONE = '{mocked_update_telefone}'
        AND CPF = '{mocked_update_cpf}'
        AND ENDERECO = '{mocked_update_endereco}'
        AND DATA_NASCIMENTO = '{mocked_update_data_nascimento}'
        """

        response = connection.execute(text(sql))
        registry = response.fetchone()

        # Update the client's name
        clientes_repositorys.update_cliente(registry.id, "telefone", "62982488163")

        # Fetch the updated client from the database
        updated_sql = f"""
            SELECT * FROM CLIENTES
            WHERE NOME = '{mocked_update_nome}'
            AND TELEFONE = '62982488163'
            AND CPF = '{mocked_update_cpf}'
            AND ENDERECO = '{mocked_update_endereco}'
            AND DATA_NASCIMENTO = '{mocked_update_data_nascimento}'
            """

        updated_response = connection.execute(text(updated_sql))
        updated_r = updated_response.fetchone()

        # Assert the updated client's name is 'UPDATEIT'
        assert updated_r.nome == mocked_update_nome

        # Assert the other attributes are unchanged
        assert updated_r.telefone == "62982488163"
        assert updated_r.cpf == mocked_update_cpf
        assert updated_r.endereco == mocked_update_endereco
        assert updated_r.data_nascimento == mocked_update_data_nascimento
        print(updated_r.telefone)

        # Clean up the database
        connection.execute(text(f"DELETE FROM CLIENTES WHERE id = {registry.id}"))
        connection.commit()

    except Exception as error:

        connection.execute(text(f"DELETE FROM CLIENTES WHERE id = {registry.id}"))
        connection.commit()
        raise error



def test_insert_cliente_contato():
    # Clientes atrrs
    mocked_nome = fake.name()
    mocked_telefone = random_phone_numbers()
    mocked_cpf = fake.cpf()
    mocked_endereco = fake.address()
    mocked_data_nascimento = fake.date_of_birth(minimum_age=20, maximum_age=85)

    # Contatos attrsfake.name()
    mocked_contato_nome = fake.name()
    mocked_telefone_contato = random_phone_numbers()
    mocked_email = fake.email()

    # Repository clientes
    clientes_repositorys.insert_cliente_contato(mocked_nome,
                                                mocked_telefone,
                                                mocked_cpf,
                                                mocked_endereco,
                                                mocked_data_nascimento,
                                                mocked_contato_nome,
                                                mocked_telefone_contato,
                                                mocked_email)

    sql_clientes = """
    SELECT * FROM CLIENTES
    WHERE NOME = '{}'
    AND TELEFONE = '{}'
    AND CPF = '{}'
    AND ENDERECO = '{}'
    AND DATA_NASCIMENTO = '{}'
    """.format(mocked_nome, mocked_telefone, mocked_cpf, mocked_endereco, mocked_data_nascimento)

    sql_contatos = """
    SELECT * FROM CONTATOS
    WHERE NOME_CONTATO = '{}'
    AND TELEFONE_CONTATO = '{}'
    AND EMAIL = '{}'
    """.format(mocked_contato_nome, mocked_telefone_contato, mocked_email)

    # Clientes
    response_costumers = connection.execute(text(sql_clientes))
    registry_costumers = response_costumers.fetchall()[0]

    # Contatos
    response_contacts = connection.execute(text(sql_contatos))
    registry_contacts = response_contacts.fetchall()[0]

    # Clientes
    assert registry_costumers.nome == mocked_nome
    assert registry_costumers.telefone == mocked_telefone
    assert registry_costumers.cpf == mocked_cpf
    assert registry_costumers.endereco == mocked_endereco
    assert registry_costumers.data_nascimento == mocked_data_nascimento

    connection.execute(text(f" DELETE FROM clientes WHERE id = {registry_costumers.id}"))

    # Contatos
    assert registry_contacts.nome_contato == mocked_contato_nome
    assert registry_contacts.telefone_contato == mocked_telefone_contato
    assert registry_contacts.email == mocked_email
    connection.execute(text(f" DELETE FROM CONTATOS WHERE id_contatos = {registry_contacts.id_contatos}"))

    connection.commit()
