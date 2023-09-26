from abc import ABC, abstractmethod


class InterfaceUpdateContatos(ABC):
    @abstractmethod
    def update_contato(self,
                       id_,
                       column,
                       update_):
        raise Exception("Must Implement this method")
