from abc import ABC, abstractmethod


class DbInterfaceContatos:

    @abstractmethod
    def add_contato_to_cliente(self,id_cliente,
                               nome_contato,
                               telefone_contato,
                               email_contato):
        pass

    @abstractmethod
    def update_contato(self, id_, contatos, column, update_):
        pass

    @abstractmethod
    def get_contatos(self, contatos):
        pass

    @abstractmethod
    def delete_contato(self, tb_contatos, id_):
        pass

    @abstractmethod
    def select_contato(self):
        pass
