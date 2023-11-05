from src.presentation.controllers.contatos.update_contato_controller import UpdateContatoController
from src.domain.infra.repository.contatos_repository import ContatosRepository
from src.usecase.contatos.update_contato import UpdateContatos


def update_contato_composer():
    repository = ContatosRepository()
    use_case = UpdateContatos(repository)
    controller = UpdateContatoController(use_case)

    return controller.handle

