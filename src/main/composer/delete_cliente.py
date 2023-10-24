from src.domain.repository.clientes_repository import ClientesRepository
from src.usecase.clientes.delete_cliente import DeleteCliente


def vanish_costumer():
    cliente_repository = ClientesRepository()
    delete_clientes = DeleteCliente(cliente_repository)
    return delete_clientes



