from src.domain.core.clientes_core import Clientes
from src.domain.core.contatos_core import Contatos
from abc import ABC, abstractmethod
from typing import List


class DbInterfaceClientes(ABC):

    @abstractmethod
    def insert_cliente_contato(self,
                               nome_cliente,
                               telefone_cliente,
                               cpf_cliente,
                               endereco_cliente,
                               data_nascimento_cliente,
                               nome_contato,
                               telefone_contato,
                               email_contato):
        pass

    @abstractmethod
    def get_clientes(self, clientes) -> List[Clientes]:
        pass

    @abstractmethod
    def get_clientes_contatos(self, clientes, contatos) -> List[Contatos]:
        pass

    @abstractmethod
    def delete_cliente(self, tb_clientes, id_) -> bool:
        pass

    @abstractmethod
    def update_cliente(self, id_, clientes, column, update_) -> bool:
        pass
