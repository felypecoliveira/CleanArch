from src.domain.actions.db_actions_clientes import DatabaseActionsClientes, DbInterfaceClientes
from src.domain.usecase.clientes.clientes_usecase import ClientesUseCase
import inject


class PostgresAdptClientes:

    @inject.autoparams()
    def __init__(self, db: DatabaseActionsClientes):
        self.db = db

    def insert_cliente_contato(self,
                               nome_cliente,
                               telefone_cliente,
                               cpf_cliente,
                               endereco_cliente,
                               data_nascimento_cliente,
                               nome_contato,
                               telefone_contato,
                               email_contato):
        self.db.insert_cliente_contato(
            nome_cliente,
            telefone_cliente,
            cpf_cliente,
            endereco_cliente,
            data_nascimento_cliente,
            nome_contato,
            telefone_contato,
            email_contato)

    def get_clientes(self, clientes):
        self.db.get_clientes(clientes)

    def get_clientes_contatos(self, clientes, contatos):
        self.db.get_clientes_contatos(clientes, contatos)

    def delete_cliente(self,tb_clientes,id_) -> bool:
        self.db.delete_cliente(tb_clientes,id_)

    def update_cliente(self,id_,to_update) -> bool:
        self.db.update_cliente(id_,to_update)


def ioc_config_clientes(binder):
    binder.bind(DbInterfaceClientes, ClientesUseCase)


def register_ioc_clientes():
    inject.configure(ioc_config_clientes)


