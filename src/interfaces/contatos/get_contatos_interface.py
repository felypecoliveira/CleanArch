from src.domain.model.contatos import ContatosDominio
from abc import ABC, abstractmethod


class InterfaceGetContatos(ABC):
    @abstractmethod
    def get_contatos(self) -> ContatosDominio:
        raise Exception("Must implement this method")
