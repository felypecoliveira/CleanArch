from src.presentation.controllers.contatos.select_contato_controller import SelectContatoController
from src.domain.infra.repository.contatos_repository import ContatosRepository
from src.usecase.contatos.select_contato import SelectContato


def select_contato_composer():
    repository = ContatosRepository()
    use_case = SelectContato(repository)
    controller = SelectContatoController(use_case)

    return controller.handle
