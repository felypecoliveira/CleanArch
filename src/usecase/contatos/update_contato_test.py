from src.infra.tests.contato_repository import ContatosRepositorySpy
from update_contato import UpdateContatos


def test_update_contato():
    id = 32
    column = "telefone_contato"
    update = "62992727161"
    repository = ContatosRepositorySpy()
    registro = UpdateContatos(repository)


    transaction = repository.update_contato(id,column,update)
    response = registro.update_contato(id, column, update)


    assert transaction.telefone_contato == update
    assert response["message"] == "update sucessfuly completed"