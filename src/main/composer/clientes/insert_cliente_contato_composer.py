from src.presentation.controllers.clientes.insert_cls_cts_controller import InsertClientesContatosController
from src.usecase.clientes.insert_cliente_contato import InsertClienteContato as UseCaseInsertClienteContato
from src.domain.repository.clientes_repository import ClientesRepository


def insert_cliente_contato_composer():
    repository = ClientesRepository()
    use_case = UseCaseInsertClienteContato(repository)
    controller = InsertClientesContatosController(use_case)

    return controller.handle
