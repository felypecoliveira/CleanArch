from abc import ABC, abstractmethod
from src.domain.models.contatos import Contatos


class InterfaceSelectContato(ABC):
    @abstractmethod
    def select_contato(self, id_) -> Contatos:
        raise Exception("Must implement this method")
