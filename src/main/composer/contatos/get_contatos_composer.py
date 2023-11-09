from src.presentation.controllers.contatos.get_contatos_controller import GetContatosController
from src.infra.repository.contatos_repository import ContatosRepository
from src.usecase.contatos.get_contatos import GetContatos


def get_contatos_composer():
    repository = ContatosRepository()
    use_case = GetContatos(repository)
    controller = GetContatosController(use_case)

    return controller.handle





