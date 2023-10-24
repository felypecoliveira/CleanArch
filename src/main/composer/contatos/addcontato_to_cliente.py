from src.presentation.controllers.contatos.add_contato_controller import AddContatoController
from src.domain.repository.contatos_repository import ContatosRepository
from src.usecase.contatos.addcontato_to_cliente import AddContatoCliente


def add_contato_to_cliente_composer():
    repository = ContatosRepository()
    use_case = AddContatoCliente(repository)
    controller = AddContatoController(use_case)

    return controller.handle


