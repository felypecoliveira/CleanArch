from src.main.interfaces.contatos_repository_interface import ContatosRepositoryInterface
from src.interfaces.get_contatos import InterfaceGetContatos


class GetContatos(InterfaceGetContatos):
    def __init__(self, contatos_repository: ContatosRepositoryInterface):
        self.contatos_repository = contatos_repository

    def get_contatos(self):
        self.contatos_repository.get_contatos()


