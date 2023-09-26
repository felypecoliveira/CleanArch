from abc import ABC, abstractmethod
from src.domain.models.contatos import Contatos


class InterfaceGetContatos(ABC):
    @abstractmethod
    def get_contatos(self) -> Contatos:
        raise Exception("Must implement this method")
