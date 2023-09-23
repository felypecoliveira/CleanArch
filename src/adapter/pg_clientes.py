from src.actions.db_actions_clientes import DatabaseActionsClientes, DbInterfaceClientes
from src.domain.usecase.clientes.clientes_usecase import ClientesUseCase
import inject


class PostgresAdptClientes:

    @inject.autoparams()
    def __init__(self, db_clientes: DatabaseActionsClientes):
        self.db_clientes = db_clientes

    def insert_cliente_contato(self,
                               nome_cliente,
                               telefone_cliente,
                               cpf_cliente,
                               endereco_cliente,
                               data_nascimento_cliente,
                               nome_contato,
                               telefone_contato,
                               email_contato):
        self.db_clientes.insert_cliente_contato(
            nome_cliente,
            telefone_cliente,
            cpf_cliente,
            endereco_cliente,
            data_nascimento_cliente,
            nome_contato,
            telefone_contato,
            email_contato)

    def get_clientes(self, clientes):
        self.db_clientes.get_clientes(clientes)

    def get_clientes_contatos(self, clientes, contatos):
        self.db_clientes.get_clientes_contatos(clientes, contatos)

    def delete_cliente(self, tb_clientes, id_) -> bool:
        self.db_clientes.delete_cliente(tb_clientes, id_)

    def update_cliente(self, id_, tb_clientes, column, update_) -> bool:
        self.db_clientes.update_cliente(id_, tb_clientes, column, update_)


def ioc_config_clientes(binder):
    binder.bind(DbInterfaceClientes, ClientesUseCase())


def register_ioc_clientes():
    inject.configure(ioc_config_clientes)


if __name__ == '__main__':
    register_ioc_clientes()
    adpt_clientes = PostgresAdptClientes()
