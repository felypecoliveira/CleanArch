from src.interfaces.select_contato import InterfaceSelectContato
from src.main.interfaces.contatos_repository_interface import ContatosRepositoryInterface
from src.domain.repository.contatos_repository import ContatosRepository
from src.domain.models.contatos import Contatos
from typing import List


class SelectContato(InterfaceSelectContato):
    # ID do cliente para verificar sua lista
    # de contatos
    def __init__(self, contatos_repository: ContatosRepositoryInterface):
        self.contatos_repository = contatos_repository

    def select_contato(self, id_) -> List[Contatos]:
        self.contatos_repository.select_contato(id_)
