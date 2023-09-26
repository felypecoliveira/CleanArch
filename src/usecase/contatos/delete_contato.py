from src.interfaces.delete_contato import InterfaceDeleteContato
from src.main.interfaces.contatos_repository_interface import ContatosRepositoryInterface


class DeleteContatos(InterfaceDeleteContato):
    def __init__(self, contatos_repository: ContatosRepositoryInterface):
        self.contatos_repository = contatos_repository

    def delete_contato(self, id_: int) -> bool:
        self.contatos_repository.delete_contato(id_)


