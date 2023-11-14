from src.infra.db.connect_settings import ConnectionHandler
from clientes_repository import ClientesRepository
from sqlalchemy import text
from faker import Faker
import random

repository = ClientesRepository()
db_connection_handler = ConnectionHandler()
connection = db_connection_handler.get_engine().connect()
fake = Faker("pt_BR")




def test_select_cliente_by_name():
    try:
        # Inserindo clientes
        mock_select_nome = fake.name()
        mock_select_telefone = random_phone_numbers()
        mock_select_cpf = fake.cpf()
        mock_select_endereco = fake.address()
        mock_select_data_nascimento = fake.date_of_birth(minimum_age=20, maximum_age=85)

        # Inserindo contatos
        mock_select_nome_contato = fake.name()
        mock_select_contato_telefone = random_phone_numbers()
        mock_select_email = fake.email()

        repository.insert_cliente_contato(
            mock_select_nome,
            mock_select_telefone,
            mock_select_cpf,
            mock_select_endereco,
            mock_select_data_nascimento,
            mock_select_nome_contato,
            mock_select_contato_telefone,
            mock_select_email
        )

        inserting = f"""
               SELECT * FROM CLIENTES
               WHERE NOME = '{mock_select_nome}'
               AND TELEFONE = '{mock_select_telefone}'
               AND CPF = '{mock_select_cpf}'
               AND ENDERECO = '{mock_select_endereco}'
               AND DATA_NASCIMENTO = '{mock_select_data_nascimento}'
               """

        response = connection.execute(text(inserting))
        registry = response.fetchone()

        repository.select_cliente_by_name(registry.nome)

        after_select = f"""
        SELECT NOME FROM CLIENTES
        WHERE NOME = '{mock_select_nome}'
        """

        select_response = connection.execute(text(after_select))
        registry_selection = select_response.fetchone()[0]

        assert registry_selection == mock_select_nome

        connection.execute(text(f"DELETE FROM CLIENTES WHERE id = {registry.id}"))
        connection.commit()

    except Exception:
        connection.execute(text(f"DELETE FROM CLIENTES WHERE id = {registry.id}"))
        connection.commit()


def teste_delete_cliente():
    try:
        # Clientes atributos
        mock_deleted_nome = fake.name()
        mock_deleted_telefone = random_phone_numbers()
        mock_deleted_cpf = fake.cpf()
        mock_deleted_endereco = fake.address()
        mock_deleted_data_nascimento = fake.date_of_birth(minimum_age=20, maximum_age=85)

        # Contatos atributos
        mock_deleted_nome_contato = fake.name()
        mock_deleted_telefone_contato = random_phone_numbers()
        mock_deleted_email = fake.email()

        # Inserindo clientes para exclusão
        repository.insert_cliente_contato(
            mock_deleted_nome,
            mock_deleted_telefone,
            mock_deleted_cpf,
            mock_deleted_endereco,
            mock_deleted_data_nascimento,
            mock_deleted_nome_contato,
            mock_deleted_telefone_contato,
            mock_deleted_email
        )

        inserting = f"""
        SELECT * FROM CLIENTES
        WHERE NOME = '{mock_deleted_nome}'
        AND TELEFONE = '{mock_deleted_telefone}'
        AND CPF = '{mock_deleted_cpf}'
        AND ENDERECO = '{mock_deleted_endereco}'
        AND DATA_NASCIMENTO = '{mock_deleted_data_nascimento}'
        """

        # Executando transação de inserção
        response = connection.execute(text(inserting))
        registry = response.fetchone()


        after_deleted = f"""
        SELECT * FROM CLIENTES
        WHERE NOME = '{mock_deleted_nome}'
        AND TELEFONE = '{mock_deleted_telefone}'
        AND CPF = '{mock_deleted_cpf}'
        AND ENDERECO = '{mock_deleted_endereco}'
        AND DATA_NASCIMENTO = '{mock_deleted_data_nascimento}'
        """

        after_transaction = connection.execute(text(after_deleted))
        registry_deleted_transaction = after_transaction.fetchone()

        print(registry_deleted_transaction)

        assert registry_deleted_transaction is None

    except Exception:
        connection.execute(text(f"DELETE FROM CLIENTES WHERE id = {registry.id}"))
        connection.commit()


def test_update_cliente():
    try:
        # Clientes atributos
        mock_update_nome = fake.name()
        mock_update_telefone = random_phone_numbers()
        mock_update_cpf = fake.cpf()
        mock_update_endereco = fake.address()
        mock_update_data_nascimento = fake.date_of_birth(minimum_age=20, maximum_age=85)

        # Contatos atributos
        mock_update_contato_nome = fake.name()
        mock_update_telefone_contato = random_phone_numbers()
        mock_update_email = fake.email()

        # Inserindo clientes e contatos
        repository.insert_cliente_contato(
            mock_update_nome,
            mock_update_telefone,
            mock_update_cpf,
            mock_update_endereco,
            mock_update_data_nascimento,
            mock_update_contato_nome,
            mock_update_telefone_contato,
            mock_update_email
        )

        sql = f"""
        SELECT * FROM CLIENTES
        WHERE NOME = '{mock_update_nome}'
        AND TELEFONE = '{mock_update_telefone}'
        AND CPF = '{mock_update_cpf}'
        AND ENDERECO = '{mock_update_endereco}'
        AND DATA_NASCIMENTO = '{mock_update_data_nascimento}'
        """

        response = connection.execute(text(sql))
        registry = response.fetchone()

        # Update the client's name
        repository.update_cliente(registry.id, "telefone", "62982488163")

        # Fetch the updated client from the database
        updated_sql = f"""
            SELECT * FROM CLIENTES
            WHERE NOME = '{mock_update_nome}'
            AND TELEFONE = '62982488163'
            AND CPF = '{mock_update_cpf}'
            AND ENDERECO = '{mock_update_endereco}'
            AND DATA_NASCIMENTO = '{mock_update_data_nascimento}'
            """

        updated_response = connection.execute(text(updated_sql))
        updated_r = updated_response.fetchone()

        # Assert the updated client's name is 'UPDATEIT'
        assert updated_r.nome == mock_update_nome

        # Assert the other attributes are unchanged
        assert updated_r.telefone == "62982488163"
        assert updated_r.cpf == mock_update_cpf
        assert updated_r.endereco == mock_update_endereco
        assert updated_r.data_nascimento == mock_update_data_nascimento
        print(updated_r.telefone)

        # Clean up the database
        connection.execute(text(f"DELETE FROM CLIENTES WHERE id = {registry.id}"))
        connection.commit()

    except Exception:

        connection.execute(text(f"DELETE FROM CLIENTES WHERE id = {registry.id}"))
        connection.commit()


def test_insert_cliente_contato():
    try:
        # Clientes atrrs
        mock_nome = fake.name()
        mock_telefone = random_phone_numbers()
        mock_cpf = fake.cpf()
        mock_endereco = fake.address()
        mock_data_nascimento = fake.date_of_birth(minimum_age=20, maximum_age=85)

        # Contatos attrsfake.name()
        mock_contato_nome = fake.name()
        mock_telefone_contato = random_phone_numbers()
        mock_email = fake.email()

        # Repository clientes
        repository.insert_cliente_contato(mock_nome,
                                                    mock_telefone,
                                                    mock_cpf,
                                                    mock_endereco,
                                                    mock_data_nascimento,
                                                    mock_contato_nome,
                                                    mock_telefone_contato,
                                                    mock_email)

        sql_clientes = """
        SELECT * FROM CLIENTES
        WHERE NOME = '{}'
        AND TELEFONE = '{}'
        AND CPF = '{}'
        AND ENDERECO = '{}'
        AND DATA_NASCIMENTO = '{}'
        """.format(mock_nome, mock_telefone, mock_cpf, mock_endereco, mock_data_nascimento)

        sql_contatos = """
        SELECT * FROM CONTATOS
        WHERE NOME_CONTATO = '{}'
        AND TELEFONE_CONTATO = '{}'
        AND EMAIL = '{}'
        """.format(mock_contato_nome, mock_telefone_contato, mock_email)

        # Clientes
        response_costumers = connection.execute(text(sql_clientes))
        registry_costumers = response_costumers.fetchall()[0]

        # Contatos
        response_contacts = connection.execute(text(sql_contatos))
        registry_contacts = response_contacts.fetchall()[0]

        # Clientes
        assert registry_costumers.nome == mock_nome
        assert registry_costumers.telefone == mock_telefone
        assert registry_costumers.cpf == mock_cpf
        assert registry_costumers.endereco == mock_endereco
        assert registry_costumers.data_nascimento == mock_data_nascimento

        connection.execute(text(f" DELETE FROM clientes WHERE id = {registry_costumers.id}"))

        # Contatos
        assert registry_contacts.nome_contato == mock_contato_nome
        assert registry_contacts.telefone_contato == mock_telefone_contato
        assert registry_contacts.email == mock_email
        connection.execute(text(f" DELETE FROM CONTATOS WHERE id_contatos = {registry_contacts.id_contatos}"))

        connection.commit()

    except Exception:
        connection.execute(text(f" DELETE FROM clientes WHERE id = {registry_costumers.id}"))
        connection.commit()



def random_phone_numbers():
    prefixos = ["62", "66"]
    prefixo = random.choice(prefixos)
    resto_n = random.randint(10000000, 99999999)
    return f'{prefixo}{resto_n}'
