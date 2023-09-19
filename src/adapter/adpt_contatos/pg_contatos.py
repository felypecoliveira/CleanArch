from src.domain.actions.db_actions_contatos import DbActionsContatos
from src.interfaces.contatos_interface import DbInterfaceContatos
from src.domain.usecase.contatos.contatos_usecase import ContatosUseCase
import inject


class PostgresAdptContatos:
    @inject.autoparams()
    def __init__(self, db_contatos: DbActionsContatos):
        self.db_contatos = db_contatos

    def add_contato_to_cliente(self):
        pass

    def update_contato(self):
        pass

    def get_contatos(self):
        pass

    def delete_contato(self):
        pass

    def select_contato(self):
        pass

def ioc_config_contatos(binder):
    binder.bind(DbInterfaceContatos, ContatosUseCase)


def register_ioc_contatos():
    inject.configure(ioc_config_contatos)
