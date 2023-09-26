from abc import ABC, abstractmethod
from src.domain.models.contatos import Contatos


class InterfaceDeleteContato(ABC):
    @abstractmethod
    def delete_contato(self,id_: int) -> bool:
        raise Exception("Must implement this method")
