from src.domain.settings.connect_settings import *
from src.domain.core.clientes import Clientes as EntityClientes
from src.domain.core.contatos import Contatos as EntityContatos
from src.main.interfaces.contatos_repository_interface import ContatosRepositoryInterface as Interface
from src.domain.models.contatos import Contatos


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
                       id_: int,
                       column: Contatos,
                       update_: str) -> bool:
        ...

    def get_contatos(self):
        with ConnectionHandler() as database:
            try:

                stmt = select(EntityContatos) \
                    .order_by(EntityContatos.id_contatos)
                objects = database.session.scalars(stmt).all()
                print(objects)




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

                for r2 in resultado2:
                    print(f"Nome = {r2.nome_contato}\n"
                          f"Telefone = {r2.telefone}\n"
                          f"Email = {r2.email}")
                    print("")
                print(f"Total de {len(resultado2)} contatos")

            except Exception as exception:
                database.session.rollback()
                raise exception
