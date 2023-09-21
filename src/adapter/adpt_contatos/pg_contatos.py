from src.actions.db_actions_contatos import DbActionsContatos
from src.interfaces.contatos_interface import DbInterfaceContatos
from src.domain.usecase.contatos.contatos_usecase import ContatosUseCase
import inject


class PostgresAdptContatos:
    @inject.autoparams()
    def __init__(self, db_contatos: DbActionsContatos):
        self.db_contatos = db_contatos

    def add_contato_to_cliente(self, id_cliente,
                               nome_contato,
                               telefone_contato,
                               email_contato):
        self.db_contatos.add_contato_to_cliente(
            id_cliente,
            nome_contato,
            telefone_contato,
            email_contato
        )

    def update_contato(self, id_, contatos, column, update_):
        self.db_contatos.update_contato(id_,
                                        contatos,
                                        column,
                                        update_)

    def get_contatos(self, contatos):
        self.db_contatos.get_contatos(contatos)

    def delete_contato(self, tb_contatos, id_):
        self.db_contatos.delete_contato(tb_contatos, id_)

    def select_contato(self):
        self.db_contatos.select_contato()


def ioc_config_contatos(binder):
    binder.bind(DbInterfaceContatos, ContatosUseCase())


def register_ioc_contatos():
    inject.configure(ioc_config_contatos)


if __name__ == '__main__':
    register_ioc_contatos()
    adpt_contatos = PostgresAdptContatos()
