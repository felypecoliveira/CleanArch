from src.infra.tests.contato_repository import ContatosRepositorySpy
from select_contato import SelectContato



def test_select_contato():
    id_cliente = 32
    repository = ContatosRepositorySpy()
    registro = SelectContato(repository)
    response = registro.select_contato(id_cliente)

    print(response)