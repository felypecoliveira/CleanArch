from src.main.interfaces.clientes_repository_interface import ClientesRepositoryInterface as Interface
from src.domain.settings.connect_settings import *
from src.domain.core.clientes import Clientes as EntityClientes
from src.domain.core.contatos import Contatos as EntityContatos
from src.domain.models.clientes import Clientes
from src.domain.models.contatos import Contatos
from datetime import date
from typing import List


class ClientesRepository(Interface):

    def insert_cliente_contato(self,
                               nome: str,
                               telefone: str,
                               cpf: str,
                               endereco: str,
                               data_nascimento: date,
                               nome_contato: str,
                               telefone_contato: str,
                               email_contato: str) -> Clientes:

        with ConnectionHandler() as database:
            try:
                cliente_registry = EntityClientes(
                    nome,
                    telefone,
                    cpf,
                    endereco,
                    data_nascimento)

                contato_registry = EntityContatos(
                    nome_contato,
                    telefone_contato,
                    email_contato
                )

                cliente_registry.contatos.append(contato_registry)
                database.session.add(cliente_registry)
                database.session.add(contato_registry)
                database.session.commit()

            except Exception as exception:
                database.session.rollback()
                raise exception

    def get_clientes(self) -> Clientes:
        with ConnectionHandler() as database:
            try:
                stmt = select(EntityClientes).order_by(EntityClientes.id)
                objetos = database.session.scalars(stmt).all()
                return objetos

            except Exception as exception:
                database.session.rollback()
                raise exception

    def get_clientes_contatos(self):
        with ConnectionHandler() as database:
            try:
                stmt = select(EntityClientes, EntityContatos) \
                    .join(EntityClientes.contatos) \
                    .order_by(EntityClientes.id, EntityContatos.id_contatos)

                row_list = []
                for row in database.session.execute(stmt):
                    row_list.append(row)

                return row_list

            except Exception as exception:
                database.session.rollback()
                raise exception

    def delete_cliente(self, id_: int) -> bool:
        with ConnectionHandler() as database:
            try:
                database.session.execute(
                    delete(EntityClientes)
                    .where(EntityClientes.id == id_)
                )

                database.session.flush()
                database.session.commit()



            except Exception as exception:
                database.session.rollback()
                raise exception

    def update_cliente(self,
                       id_: int,
                       column: str,
                       update_: str | date) -> bool:
        with ConnectionHandler() as database:
            try:
                database.session.execute(
                    update(EntityClientes),
                    [
                        {"id": id_, column: update_}
                    ]
                )

                database.session.commit()

            except Exception as exception:
                database.session.rollback()
                raise exception
