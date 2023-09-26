from abc import ABC, abstractmethod
from src.domain.models.clientes import Clientes

from typing import List


class InterfaceGetCliente(ABC):
    @abstractmethod
    def get_clientes(self) -> List[Clientes]:
        raise Exception("Must implement this method")
