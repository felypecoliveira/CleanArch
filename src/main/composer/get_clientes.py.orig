from src.domain.repository.clientes_repository import ClientesRepository
from src.usecase.clientes.get_clientes import GetClientes


def clientes():
    clientes_repository = ClientesRepository()
    getclientes = GetClientes(clientes_repository)

    return getclientes

