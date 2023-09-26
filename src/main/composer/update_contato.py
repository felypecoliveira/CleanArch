from src.domain.repository.contatos_repository import ContatosRepository
from src.usecase.contatos.update_contato import UpdateContatos


def updater_contacts():
    clientes_repository = ContatosRepository()
    update_contatos = UpdateContatos(clientes_repository)

    return update_contatos


updater_contacts().update_contato(1, '', '')
