from abc import ABC, abstractmethod
from src.domain.infra.model.contatos import ContatosDominio


class ContatosRepositoryInterface(ABC):

    @abstractmethod
    def add_contato_to_cliente(self,
                               id: int,
                               nome_contato: str,
                               telefone: str,
                               email: str):
        raise Exception(f"Must implement all methods from the interface related ")

    @abstractmethod
    def update_contato(self,
                       id: int,
                       column: ContatosDominio,
                       update_: str):
        raise Exception(f"Must implement all methods from the interface related ")

    @abstractmethod
    def get_contatos(self):
        raise Exception(f"Must implement all methods from the interface related ")

    @abstractmethod
    def delete_contato(self, id_: int):
        raise Exception(f"Must implement all methods from the interface related ")

    @abstractmethod
    def select_contato(self, id_):
        raise Exception(f"Must implement all methods from the interface related ")



