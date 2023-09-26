from abc import ABC, abstractmethod
from datetime import date
from src.domain.models.clientes import Clientes
from src.domain.models.contatos import Contatos


class ClientesRepositoryInterface(ABC):
    @abstractmethod
    def insert_cliente_contato(self,
                               nome: str,
                               telefone: str,
                               cpf: str,
                               endereco: str,
                               data_nascimento: date,
                               nome_contato: str,
                               telefone_contato: str,
                               email_contato: str) -> Clientes:
        raise Exception("Must implement this method insert_cliente_contato")

    @abstractmethod
    def get_clientes(self) -> Clientes:
        raise Exception("Must implement this method get_clientes")

    @abstractmethod
    def get_clientes_contatos(self):
        raise Exception("Must implement this method get_clientes_contatos")

    @abstractmethod
    def delete_cliente(self, id_: int) -> bool:
        raise Exception("Must implement this method delete_cliente")

    @abstractmethod
    def update_cliente(self,
                       id_: int,
                       column: Clientes,
                       update_: str | date) -> bool:
        pass
