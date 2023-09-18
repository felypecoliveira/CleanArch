from abc import ABC, abstractmethod


class DbInterfaceContatos:

    @abstractmethod
    def add_contato_to_cliente(self):
        pass

    @abstractmethod
    def update_contato(self):
        pass

    @abstractmethod
    def get_contatos(self):
        pass

    @abstractmethod
    def delete_contato(self):
        pass

    @abstractmethod
    def select_contato(self):
        pass
