from src.presentation.controllers.clientes.get_cliente_contatos_controller import GetClientesContatosController
from src.usecase.clientes.get_cliente_contatos import GetClientesContatos
from src.domain.infra.repository.clientes_repository import ClientesRepository


def get_cliente_contatos_composer():
    repository = ClientesRepository()
    use_case = GetClientesContatos(repository)
    controller = GetClientesContatosController(use_case)

    return controller.handle




