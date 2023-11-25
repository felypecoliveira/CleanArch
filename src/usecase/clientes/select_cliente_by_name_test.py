from src.infra.tests.cliente_repository import ClientesRespositorySpy
from select_cliente_by_name import SelectClienteName


def test_select_cliente_by_name():
    try:
        nome = "Roberto Leal Magalhaes"
        repository = ClientesRespositorySpy()
        registro = SelectClienteName(repository)
        select = registro.select_cliente_by_name(nome)
        assert repository.select_cliente_by_name(nome)
        assert select["sucess"] is  True


    except Exception as error:
        assert str(error) == "Nome não conter caracteres especiais"
        ...