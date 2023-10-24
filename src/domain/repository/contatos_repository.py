from src.main.interfaces.contatos_repository_interface import ContatosRepositoryInterface as Interface
from src.domain.entities.clientes import Clientes as EntityClientes
from src.domain.entities.contatos import Contatos as EntityContatos
from src.domain.infra.db.connect_settings import *


class ContatosRepository(Interface):
    def add_contato_to_cliente(self,
                               id: int,
                               nome_contato: str,
                               telefone: str,
                               email: str):
        with ConnectionHandler() as database:
            try:
                q = database.session \
                    .query(EntityClientes) \
                    .filter(EntityClientes.id == id).all()

                primeiro_cliente = q[0]

                primeiro_cliente.contatos.append(EntityContatos(nome_contato,
                                                                telefone,
                                                                email))

                database.session.commit()


            except Exception as exception:
                database.session.rollback()
                raise exception

    def update_contato(self,
                       id: int,
                       column: str,
                       update_: str) -> bool:
        with ConnectionHandler() as database:
            try:
                database.session.execute(
                    update(EntityContatos),
                    [
                        {"id_contatos": id, column: update_}
                    ]
                )

                database.session.commit()

            except Exception as exception:
                raise exception

    def get_contatos(self):
        with ConnectionHandler() as database:
            try:
                stmt = select(EntityContatos).order_by(EntityContatos.id_contatos)
                objects = database.session.scalars(stmt).all()
                return objects

            except Exception as exception:
                database.session.rollback()
                raise exception

        ...

    def delete_contato(self, id_: int):
        with ConnectionHandler() as database:
            try:

                database.session.execute(
                    delete(EntityContatos)
                    .where(EntityContatos.id_contatos == id_)
                )

                database.session.flush()
                database.session.commit()


            except Exception as exception:
                database.session.rollback()
                raise exception
        ...

    def select_contato(self, id_):
        with ConnectionHandler() as database:
            try:
                q = database.session \
                    .query(EntityClientes) \
                    .filter(EntityClientes.id == id_)

                resultado = q.all()

                for r in resultado:
                    q2 = database.session \
                        .query(EntityContatos) \
                        .filter(EntityContatos.id_cliente == r.id)

                resultado2 = q2.all()

                lista_contatos = []
                for r2 in resultado2:
                    lista_contatos.append(r2.id_contatos)
                    lista_contatos.append(r2.nome_contato)
                    lista_contatos.append(r2.telefone_contato)
                    lista_contatos.append(r2.email)

                return lista_contatos

            except Exception as exception:
                database.session.rollback()
