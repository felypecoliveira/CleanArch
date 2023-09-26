from abc import abstractmethod, ABC
from src.domain.models.clientes import Clientes
from datetime import date


class InterfaceClienteContato(ABC):
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

        raise Exception(f"Must Implement this method")
