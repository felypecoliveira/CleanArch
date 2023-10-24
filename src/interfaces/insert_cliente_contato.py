from src.domain.infra.model.clientes import ClientesDominio
from abc import abstractmethod, ABC
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
                               email: str) -> ClientesDominio:

        raise Exception(f"Must Implement this method")
