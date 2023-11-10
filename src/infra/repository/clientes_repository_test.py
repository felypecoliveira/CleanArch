from src.infra.db.connect_settings import ConnectionHandler
from clientes_repository import ClientesRepository
from sqlalchemy import text

db_connection_handler = ConnectionHandler()
connection = db_connection_handler.get_engine().connect()


def test_update_cliente():
    clientes_repositorys = ClientesRepository()


def select_cliente_by_name():
    clientes_repositorys = ClientesRepository()


def test_insert_cliente_contato():
    # Clientes atrrs
    mocked_nome = "First-"
    mocked_telefone = "62985785500"
    mocked_cpf = "05110918180"
    mocked_endereco = "Av dos cantinhos serra alta"
    mocked_data_nascimento = "1989-05-10"

    # Contatos attrs

    mocked_contato_nome = "Gustavo Mendes Souza"
    mocked_telefone_contato = "62988452311"
    mocked_email = "andorinhas123@gmail.com"

    # Repository clientes
    clientes_repositorys = ClientesRepository()

    clientes_repositorys.insert_cliente_contato(mocked_nome,
                                                mocked_telefone,
                                                mocked_cpf,
                                                mocked_endereco,
                                                mocked_data_nascimento,
                                                mocked_contato_nome,
                                                mocked_telefone_contato,
                                                mocked_email)

    sql = f"""
    SELECT  CL.NOME, 
            CL.TELEFONE, 
		    CL.CPF,  
		    CLI.ENDERECO, 
		    CL.DATA_NASCIMENTO,
            CT.NOME_CONTATO,
            CT.TELEFONE_CONTATO, 
            CT.EMAIL
            FROM CLIENTE
            INNER JOIN CONTATO
            ON CL.ID = CT.ID_CLIENTE;
    """

    response = connection.execute(text(sql))
    registry = response.fetchall()[0]

    assert registry.nome == mocked_nome
    assert registry.telefone == mocked_telefone
    assert registry.cpf == mocked_cpf
    assert registry.endereco == mocked_endereco
    assert registry.data_nascimento == mocked_data_nascimento
    assert registry.nome_contato == mocked_contato_nome
    assert registry.telefone_contato == mocked_telefone_contato
    assert registry.email == mocked_email

    connection.execute(text(f" DELETE FROM CLIENTES WHERE ID == {registry.id}"))
    connection.commit()

    def get_clientes():
        clientes_repositorys = ClientesRepository()

    def get_clientes_contatos():
        clientes_repositorys = ClientesRepository()

    def delete_cliente():
        clientes_repositorys = ClientesRepository()
