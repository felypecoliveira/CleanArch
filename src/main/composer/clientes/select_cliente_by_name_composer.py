from src.presentation.controllers.clientes.select_cliente_by_name_controller import SelectClienteByNameController
from src.usecase.clientes.select_cliente_by_name import SelectClienteName as UseCaseSelectClienteName
from src.infra.repository.clientes_repository import ClientesRepository


def select_cliente_by_name_composer():
    repository = ClientesRepository()
    use_case = UseCaseSelectClienteName(repository)
    controller = SelectClienteByNameController(use_case)

    return controller.handle