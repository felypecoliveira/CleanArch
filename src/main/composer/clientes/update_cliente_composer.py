from src.presentation.controllers.clientes.update_cliente_controller import UpdateClientesController
from src.infra.repository.clientes_repository import ClientesRepository
from src.usecase.clientes.update_cliente import UpdateCliente


def update_cliente_composer():
    repository = ClientesRepository()
    use_case = UpdateCliente(repository)
    controller = UpdateClientesController(use_case)

    return controller.handle


