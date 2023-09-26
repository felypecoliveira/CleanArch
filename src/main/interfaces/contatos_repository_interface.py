from abc import ABC, abstractmethod
from src.domain.models.contatos import Contatos


class ContatosRepositoryInterface(ABC):

    @abstractmethod
    def add_contato_to_cliente(self,
                               id: int,
                               nome_contato: str,
                               telefone: str,
                               email: str):
        ...

    @abstractmethod
    def update_contato(self,
                       id_: int,
                       column: Contatos,
                       update_: str):
        ...

    @abstractmethod
    def get_contatos(self):
        ...

    @abstractmethod
    def delete_contato(self, id_: int):
        ...

    @abstractmethod
    def select_contato(self, id_):
        ...
