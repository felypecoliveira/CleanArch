from src.domain.infra.model.clientes import ClientesDominio
from abc import ABC, abstractmethod
from typing import List



class InterfaceGetCliente(ABC):
    @abstractmethod
    def get_clientes(self) -> List[ClientesDominio]:
        raise Exception("Must implement this method")
