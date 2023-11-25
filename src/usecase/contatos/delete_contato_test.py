from src.infra.tests.contato_repository import ContatosRepositorySpy
from delete_contato import DeleteContatos


def test_delete_contato():
    id = 55
    repository = ContatosRepositorySpy()
    registro = DeleteContatos(repository)
    transaction = registro.delete_contato(id)

    print(transaction)