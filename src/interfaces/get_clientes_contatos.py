from abc import ABC, abstractmethod
from src.domain.models.contatos import Contatos
from typing import List


class InterfaceGetClientesContatos(ABC):
    @abstractmethod
    def get_clientes_contatos(self) -> List[Contatos]:
        raise Exception("Must implement this method")
