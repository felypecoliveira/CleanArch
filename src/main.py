import inject
from src.interfaces.contatos_interface import DbInterfaceContatos
from src.interfaces.clientes_interface import DbInterfaceClientes
from src.domain.usecase.contatos.contatos_usecase import ContatosUseCase
from src.domain.usecase.clientes.clientes_usecase import ClientesUseCase
from src.adapter.adpt_clientes.pg_clientes import PostgresAdptClientes
from src.adapter.adpt_contatos.pg_contatos import PostgresAdptContatos
# from src.domain.core.contatos_core import Contatos
from src.domain.core.clientes_core import Clientes


class Service:
    @inject.autoparams()
    def __init__(self, db_contatos: PostgresAdptContatos, db_clientes: PostgresAdptClientes):
        self.db_contatos = db_contatos
        self.db_clientes = db_clientes

    # METODOS PARA AÇÕES RELACIONADAS A CONTATOS
    def update_contato(self, id_, contatos, column, update_):
        self.db_contatos.update_contato(id_, contatos, column, update_)

    def get_contatos(self, contatos):
        self.db_contatos.get_contatos(contatos)

    def add_contato_to_cliente(self, id_cliente,
                               nome_contato,
                               telefone_contato,
                               email_contato):
        self.db_contatos.add_contato_to_cliente(id_cliente,
                                                nome_contato,
                                                telefone_contato,
                                                email_contato)

    def delete_contato(self, tb_contatos, id_):
        self.db_contatos.delete_contato(tb_contatos, id_)

    def select_contato(self):
        self.db_contatos.select_contato()

    # METODOS PARA AÇÕES RELACIONADAS A CLIENTES

    def insert_cliente_contato(self, nome_cliente, telefone_cliente, cpf_cliente, endereco_cliente,
                               data_nascimento_cliente,
                               nome_contato, telefone_contato, email_contato):
        self.db_clientes.insert_cliente_contato(nome_cliente, telefone_cliente, cpf_cliente, endereco_cliente,
                                                data_nascimento_cliente, nome_contato, telefone_contato,
                                                email_contato)

    def get_clientes(self, clientes):
        return self.db_clientes.get_clientes(clientes)

    def get_clientes_contatos(self, clientes, contatos):
        return self.db_clientes.get_clientes_contatos(clientes, contatos)

    def delete_cliente(self, tb_clientes, id_):
        return self.db_clientes.delete_cliente(tb_clientes, id_)

    def update_cliente(self, id_, tb_clientes, column, update_):
        return self.db_clientes.update_cliente(id_, tb_clientes, column, update_)


def configure_injection(binder):
    binder.bind(DbInterfaceContatos, ContatosUseCase())
    binder.bind(DbInterfaceClientes, ClientesUseCase())


def config_ioc():
    inject.configure(configure_injection)



if __name__ == '__main__':
    config_ioc()
    service = inject.instance(Service)
    service.get_clientes(Clientes)
