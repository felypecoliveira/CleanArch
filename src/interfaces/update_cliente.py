from abc import abstractmethod, ABC
from datetime import date


class InterfaceUpdateCliente(ABC):
    @abstractmethod
    def update_cliente(self,
                       id_: int,
                       column: str,
                       update_: str | date) -> bool:
        raise Exception("Must Implemented this method")
