from src.infra.tests.cliente_repository import ClientesRespositorySpy
from delete_cliente import DeleteCliente


def test_delete_cliente():
    id = 90

    repository = ClientesRespositorySpy()
    registro = DeleteCliente(repository)
    transaction = registro.delete_cliente(id)
    print(transaction)