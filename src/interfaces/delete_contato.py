from abc import ABC, abstractmethod


class InterfaceDeleteContato(ABC):
    @abstractmethod
    def delete_contato(self,id_: int) -> bool:
        raise Exception("Must implement this method")
