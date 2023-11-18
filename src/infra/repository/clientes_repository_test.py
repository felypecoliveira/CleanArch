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
        mock_nome = fake.name()
        mock_telefone = __random_phone_numbers()
        mock_cpf = fake.cpf()
        mock_endereco = fake.address()
        mock_data_nascimento = fake.date_of_birth(minimum_age=20,
                                                         maximum_age=85)

        # Inserindo contatos
        mock_nome_contato = fake.name()
        mock_contato_telefone = __random_phone_numbers()
        mock_email = fake.email()

        repository.insert_cliente_contato(
            mock_nome,
            mock_telefone,
            mock_cpf,
            mock_endereco,
            mock_data_nascimento,
            mock_nome_contato,
            mock_contato_telefone,
            mock_email
        )

        inserting = f"""
               SELECT * FROM CLIENTES
               WHERE NOME = '{mock_nome}'
               AND TELEFONE = '{mock_telefone}'
               AND CPF = '{mock_cpf}'
               AND ENDERECO = '{mock_endereco}'
               AND DATA_NASCIMENTO = '{mock_data_nascimento}'
               """

        response = connection.execute(text(inserting))
        registry = response.fetchone()

        repository.select_cliente_by_name(registry.nome)

        after_select = f"""
        SELECT NOME FROM CLIENTES WHERE NOME = '{mock_nome}'
        """

        select_response = connection.execute(text(after_select))
        registry_selection = select_response.fetchone()[0]

        assert registry_selection == mock_nome

        connection.execute(text(f"DELETE FROM CLIENTES "
                                f"WHERE id = {registry.id}"))
        connection.commit()

    except Exception:
        connection.execute(text(f"DELETE FROM CLIENTES "
                                f"WHERE id = {registry.id}"))
        connection.commit()


def teste_delete_cliente():
    try:
        # Clientes atributos
        mock_nome = fake.name()
        mock_telefone = __random_phone_numbers()
        mock_cpf = fake.cpf()
        mock_endereco = fake.address()
        mock_data_nascimento = fake.date_of_birth(minimum_age=20,
                                                          maximum_age=85)

        # Contatos atributos
        mock_nome_contato = fake.name()
        mock_telefone_contato = __random_phone_numbers()
        mock_email = fake.email()

        # Inserindo clientes para exclusão
        repository.insert_cliente_contato(
            mock_nome,
            mock_telefone,
            mock_cpf,
            mock_endereco,
            mock_data_nascimento,
            mock_nome_contato,
            mock_telefone_contato,
            mock_email
        )

        inserting = f"""
        SELECT * FROM CLIENTES
        WHERE NOME = '{mock_nome}'
        AND TELEFONE = '{mock_telefone}'
        AND CPF = '{mock_cpf}'
        AND ENDERECO = '{mock_endereco}'
        AND DATA_NASCIMENTO = '{mock_data_nascimento}'
        """

        # Executando transação de inserção
        response = connection.execute(text(inserting))
        registry = response.fetchone()

        after_deleted = f"""
        SELECT * FROM CLIENTES
        WHERE NOME = '{mock_nome}'
        AND TELEFONE = '{mock_telefone}'
        AND CPF = '{mock_cpf}'
        AND ENDERECO = '{mock_endereco}'
        AND DATA_NASCIMENTO = '{mock_data_nascimento}'
        """

        after_transaction = connection.execute(text(after_deleted))
        registry_deleted_transaction = after_transaction.fetchone()

        print(registry_deleted_transaction)

        assert registry_deleted_transaction is None

    except Exception:
        connection.execute(text(f"DELETE FROM CLIENTES "
                                f"WHERE id = {registry.id}"))
        connection.commit()


def test_update_cliente():
    try:
        # Clientes atributos
        mock_nome = fake.name()
        mock_telefone = __random_phone_numbers()
        mock_cpf = fake.cpf()
        mock_endereco = fake.address()
        mock_data_nascimento = fake.date_of_birth(minimum_age=20,
                                                         maximum_age=85)

        # Contatos atributos
        mock_nome_contato = fake.name()
        mock_telefone_contato = __random_phone_numbers()
        mock_email = fake.email()

        # Inserindo clientes e contatos
        repository.insert_cliente_contato(
            mock_nome,
            mock_telefone,
            mock_cpf,
            mock_endereco,
            mock_data_nascimento,
            mock_nome_contato,
            mock_telefone_contato,
            mock_email
        )

        sql = f"""
        SELECT * FROM CLIENTES
        WHERE NOME = '{mock_nome}'
        AND TELEFONE = '{mock_telefone}'
        AND CPF = '{mock_cpf}'
        AND ENDERECO = '{mock_endereco}'
        AND DATA_NASCIMENTO = '{mock_data_nascimento}'
        """

        response = connection.execute(text(sql))
        registry = response.fetchone()

        # Update the client's name
        repository.update_cliente(registry.id,
                                  "telefone",
                                  "62982488163")

        # Fetch the updated client from the database
        updated_sql = f"""
            SELECT * FROM CLIENTES
            WHERE NOME = '{mock_nome}'
            AND TELEFONE = '62982488163'
            AND CPF = '{mock_cpf}'
            AND ENDERECO = '{mock_endereco}'
            AND DATA_NASCIMENTO = '{mock_data_nascimento}'
            """

        updated_response = connection.execute(text(updated_sql))
        updated_r = updated_response.fetchone()

        assert updated_r.nome == mock_nome
        assert updated_r.telefone == "62982488163"
        assert updated_r.cpf == mock_cpf
        assert updated_r.endereco == mock_endereco
        assert updated_r.data_nascimento == mock_data_nascimento

        connection.execute(text(f"DELETE FROM CLIENTES "
                                f"WHERE id = {registry.id}"))

        connection.commit()

    except Exception:

        connection.execute(text(f"DELETE FROM CLIENTES "
                                f"WHERE id = {registry.id}"))

        connection.commit()


def test_insert_cliente_contato():
    try:
        # Clientes atrrs
        mock_nome = fake.name()
        mock_telefone = __random_phone_numbers()
        mock_cpf = fake.cpf()
        mock_endereco = fake.address()
        mock_data_nascimento = fake.date_of_birth(minimum_age=20,
                                                  maximum_age=85)

        # Contatos attrsfake.name()
        mock_contato_nome = fake.name()
        mock_telefone_contato = __random_phone_numbers()
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

        sql_clientes = f"""
        SELECT * FROM CLIENTES
        WHERE NOME = '{mock_nome}'
        AND TELEFONE = '{mock_telefone}'
        AND CPF = '{mock_cpf}'
        AND ENDERECO = '{mock_endereco}'
        AND DATA_NASCIMENTO = '{mock_data_nascimento}'
        """

        sql_contatos = f"""
        SELECT * FROM CONTATOS
        WHERE NOME_CONTATO = '{mock_contato_nome}'
        AND TELEFONE_CONTATO = '{mock_telefone_contato}'
        AND EMAIL = '{mock_email}'
        """

        # Clientes
        response_cls = connection.execute(text(sql_clientes))
        registry_cls = response_cls.fetchall()[0]

        # Contatos
        response_cts = connection.execute(text(sql_contatos))
        registry_cts = response_cts.fetchall()[0]

        # Clientes
        assert registry_cls.nome == mock_nome
        assert registry_cls.telefone == mock_telefone
        assert registry_cls.cpf == mock_cpf
        assert registry_cls.endereco == mock_endereco
        assert registry_cls.data_nascimento == mock_data_nascimento

        # Contatos
        assert registry_cts.nome_contato == mock_contato_nome
        assert registry_cts.telefone_contato == mock_telefone_contato
        assert registry_cts.email == mock_email

        connection.execute(text(f" DELETE FROM clientes "
                                f"WHERE id = {registry_cls.id}"))
        connection.commit()

    except Exception:
        connection.execute(text(f" DELETE FROM clientes "
                                f"WHERE id = {registry_cls.id}"))
        connection.commit()


def __random_phone_numbers():
    prefixos = ["62", "66"]
    prefixo = random.choice(prefixos)
    resto_n = random.randint(10000000, 99999999)
    return f'{prefixo}{resto_n}'
