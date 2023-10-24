from src.domain.infra.model.contatos import ContatosDominio
from abc import ABC, abstractmethod
from typing import List


class InterfaceGetClientesContatos(ABC):
    @abstractmethod
    def get_clientes_contatos(self) -> List[ContatosDominio]:
        raise Exception("Must implement this method")
