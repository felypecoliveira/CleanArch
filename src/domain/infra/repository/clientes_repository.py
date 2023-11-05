from src.domain.interfaces.clientes_repository_interface import ClientesRepositoryInterface as Interface
from src.domain.infra.model.clientes import ClientesDominio as clientes_domain
from src.domain.infra.model.contatos import ContatosDominio as contatos_domain
from src.domain.entities.clientes import Clientes as ClientesEntity
from src.domain.infra.db.connect_settings import *
from src.domain.entities.contatos import Contatos as ContatosEntity
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
                               email: str) -> bool:

        with ConnectionHandler() as database:
            try:
                cliente_registry = ClientesEntity(
                    nome,
                    telefone,
                    cpf,
                    endereco,
                    data_nascimento
                )

                contato_registry = ContatosEntity(
                    nome_contato,
                    telefone_contato,
                    email
                )

                cliente_registry.contatos.append(contato_registry)
                database.session.add(cliente_registry)
                database.session.add(contato_registry)
                database.session.commit()

            except Exception as exception:
                database.session.rollback()
                raise exception

    def confirm_id_cliente(self, id:int):
        with ConnectionHandler() as database:
            try:
                cliente = (
                    database.session
                    .query(ClientesEntity)
                    .filter(ClientesEntity.id == id)
                    .one()
                )
                return cliente

            except Exception as exception:
                database.session.rollback()
                raise exception

    def get_clientes(self) -> clientes_domain:
        with ConnectionHandler() as database:
            try:
                stmt = select(ClientesEntity).order_by(ClientesEntity.id)
                objetos = database.session.scalars(stmt).all()
                return objetos

            except Exception as exception:
                database.session.rollback()
                raise exception

    def get_clientes_contatos(self) -> List[contatos_domain]:
        with ConnectionHandler() as database:
            try:
                stmt = select(ClientesEntity, ContatosEntity).join(ClientesEntity.contatos) \
                    .order_by(ClientesEntity.id, ContatosEntity.id_contatos)

                row_list = []
                for row in database.session.execute(stmt):
                    row_list.append(row)

                return row_list

            except Exception as exception:
                database.session.rollback()
                raise exception

    def select_cliente_by_name(self, name: str):
        with ConnectionHandler() as database:
            try:
                cliente = (
                    database.session
                    .query(ClientesEntity)
                    .filter(ClientesEntity.nome == name)
                    .all()
                )
                return cliente

            except Exception as exception:
                database.session.rollback()
                raise exception

    def delete_cliente(self, id_: int) -> bool:
        with ConnectionHandler() as database:
            try:
                database.session.execute(
                    delete(ClientesEntity)
                    .where(ClientesEntity.id == id_)
                )

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
                    update(ClientesEntity),
                    [
                        {"id": id_, column: update_}
                    ]
                )

                database.session.commit()

            except Exception as exception:
                database.session.rollback()
                raise exception
