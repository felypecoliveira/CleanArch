from abc import ABC, abstractmethod


class InterfaceContatoCliente(ABC):
    @abstractmethod
    def add_contato_to_cliente(self,
                               id,
                               nome_contato,
                               telefone,
                               email):
        raise Exception("Must implement this method")
