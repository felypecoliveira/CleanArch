from src.domain.repository.contatos_repository import ContatosRepository
from src.usecase.contatos.delete_contato import DeleteContatos



def vanish_contacts():
    contatos_repository = ContatosRepository()
    deletion_usecase = DeleteContatos(contatos_repository)

    return deletion_usecase


