from abc import ABC, abstractmethod


class InterfaceUpdateContatos(ABC):
    @abstractmethod
    def update_contato(self,
                       id: int,
                       column: str,
                       update_: str):
        raise Exception("Must Implement this method")
