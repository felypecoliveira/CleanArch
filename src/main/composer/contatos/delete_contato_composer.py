from src.presentation.controllers.contatos.delete_contato_controller import DeleteContatoController
from src.infra.repository.contatos_repository import ContatosRepository
from src.usecase.contatos.delete_contato import DeleteContatos


def delete_contato_composer():
    repository = ContatosRepository()
    use_case = DeleteContatos(repository)
    controller = DeleteContatoController(use_case)

    return controller.handle
