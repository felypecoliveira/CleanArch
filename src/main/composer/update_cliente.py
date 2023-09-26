from src.domain.repository.clientes_repository import ClientesRepository
from src.usecase.clientes.update_cliente import UpdateCliente


def updater_costumer():
    clientes_repository = ClientesRepository()
    update_clientes = UpdateCliente(ClientesRepository)
    return update_clientes


updater_costumer().update_cliente(1,
                                          '',
                                          '')
