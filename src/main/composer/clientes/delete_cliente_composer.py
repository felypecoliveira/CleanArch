from src.presentation.controllers.clientes.delete_cliente_controller import DeleteClienteController
from src.domain.infra.repository.clientes_repository import ClientesRepository
from src.usecase.clientes.delete_cliente import DeleteCliente


def delete_cliente_composer():
    repository = ClientesRepository()
    use_case = DeleteCliente(repository)
    controller = DeleteClienteController(use_case)

    return controller.handle



