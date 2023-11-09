from src.domain.model.contatos import  ContatosDominio
from abc import ABC, abstractmethod


class InterfaceSelectContato(ABC):
    @abstractmethod
    def select_contato(self, id_: int) -> ContatosDominio:
        raise Exception(f"Must implement all methods from the interface related ")
