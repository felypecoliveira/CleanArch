from src.presentation.controllers.clientes.get_clientes_controller import GetClientesController
from src.domain.infra.repository.clientes_repository import ClientesRepository
from src.usecase.clientes.get_clientes import GetClientes


def get_clientes_composer():
    repository = ClientesRepository()
    use_case = GetClientes(repository)
    controller = GetClientesController(use_case)

    return controller.handle



