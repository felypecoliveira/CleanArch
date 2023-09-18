from src.interfaces.clientes_interface import DbInterfaceClientes
from src.domain.core.clientes_core import Clientes
from src.domain.core.contatos_core import Contatos
from typing import List
import inject


class DatabaseActionsClientes:

    @inject.autoparams()
    def __init__(self, db: DbInterfaceClientes):
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
            self,
            nome_cliente,
            telefone_cliente,
            cpf_cliente,
            endereco_cliente,
            data_nascimento_cliente,
            nome_contato,
            telefone_contato,
            email_contato
        )

    def get_clientes(self, clientes) -> List[Clientes]:
        self.db.get_clientes(self,clientes)

    def get_clientes_contatos(self, tb1,tb2) -> List[Contatos]:
        self.db.get_clientes_contatos(self,tb1, tb2)


    def delete_cliente(self,tb_clientes,id_) -> bool:
        self.db.delete_cliente(self,tb_clientes,id_)

    def update_cliente(self,id_,column_to_update):
        self.db.delete_cliente(self,id_,column_to_update)

