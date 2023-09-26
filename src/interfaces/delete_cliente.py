from abc import ABC, abstractmethod


class InterfaceDeleteCliente(ABC):
    @abstractmethod
    def delete_cliente(self, id_) -> bool:
        raise Exception("Must implement this method")
