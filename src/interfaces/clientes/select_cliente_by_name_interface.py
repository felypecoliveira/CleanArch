from abc import ABC, abstractmethod


class InterfaceSelectClienteByName(ABC):
    @abstractmethod
    def select_cliente_by_name(self, name: str):
        raise Exception(f"Must Implement this method")
