from src.domain.entities.clientes import Clientes
from src.domain.entities.contatos import Contatos
from abc import ABC, abstractmethod
from datetime import date


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
                               email: str) -> Clientes:
        raise Exception(f"Must implement all methods from the interface related ")

    @abstractmethod
    def get_clientes(self) -> Clientes:
        raise Exception(f"Must implement all methods from the interface related ")

    @abstractmethod
    def get_clientes_contatos(self) -> Contatos:
        raise Exception(f"Must implement all methods from the interface related ")

    @abstractmethod
    def delete_cliente(self, id_: int) -> bool:
        raise Exception(f"Must implement all methods from the interface related ")

    @abstractmethod
    def update_cliente(self,
                       id_: int,
                       column: Clientes,
                       update_: str | date) -> bool:
        raise Exception(f"Must implement all methods from the interface related ")



    @abstractmethod
    def select_cliente_by_name(self,name: str):
        raise Exception(f"Must implement all methods from the interface related ")

