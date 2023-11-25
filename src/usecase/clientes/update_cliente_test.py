from src.infra.tests.cliente_repository import ClientesRespositorySpy
from update_cliente import UpdateCliente


def test_update_nome_cliente():
    try:
        id = 50
        column = "nome"
        update = "ANDRE FELYPE"

        repository = ClientesRespositorySpy()
        registro = UpdateCliente(repository)

        repository_spy = repository.update_cliente(id, column, update)
        transaction = registro.update_cliente(id, column, update)

        assert  repository_spy.nome == update
        assert transaction["message"] == "update sucessfuly completed"

    except Exception as error:
        assert error
        print(error)


def test_update_telefone_cliente():
    id = 45
    column = "telefone"
    update = "62985785227"

    repository = ClientesRespositorySpy()
    registro = UpdateCliente(repository)

    repository_spy = repository.update_cliente(id, column, update)
    transaction = registro.update_cliente(id, column, update)

    assert repository_spy.telefone == update
    assert transaction["message"] == "update sucessfuly completed"



def test_update_cpf_cliente():
    id = 45
    column = "cpf"
    update = "051.109.181-80"

    repository = ClientesRespositorySpy()
    registro = UpdateCliente(repository)

    repository_spy = repository.update_cliente(id, column, update)
    transaction = registro.update_cliente(id, column, update)
    print(repository_spy.cpf)
    assert repository_spy.cpf == update
    assert transaction["message"] == "update sucessfuly completed"



def test_update_telefone_cliente():
    id = 45
    column = "telefone"
    update = "62985785227"

    repository = ClientesRespositorySpy()
    registro = UpdateCliente(repository)

    repository_spy = repository.update_cliente(id, column, update)
    transaction = registro.update_cliente(id, column, update)
    print(repository_spy.telefone)
    assert repository_spy.telefone == update
    assert transaction["message"] == "update sucessfuly completed"
