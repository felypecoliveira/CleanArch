from src.interfaces.contatos_interface import DbInterfaceContatos
from src.domain.settings.connect_settings import DbConnectionHandler
from sqlalchemy import text, select, update, delete
from src.domain.core.clientes_core import Clientes
from src.domain.core.contatos_core import Contatos


class ContatosUseCase(DbInterfaceContatos):

    def add_contato_to_cliente(self, id_cliente,
                               nome_contato,
                               telefone_contato,
                               email_contato):

        with DbConnectionHandler() as database:
            try:
                q = database.session.query(Clientes).filter(Clientes.id == id_cliente).all()
                q1 = q[0]
                q1.contatos.append(Contatos(nome_contato,
                                            telefone_contato,
                                            email_contato))

                database.session.add(q1)
                database.session.commit()

            except Exception as exception:
                database.session.rollback()
                raise exception

    def update_contato(self, id_, contatos, column, update_):
        with DbConnectionHandler() as database:
            try:

                database.session.execute(
                    update(contatos),
                    [
                        {"id_contatos": id_, column: update_}
                    ]
                )

                database.session.flush()
                database.session.commit()


            except Exception as exception:
                database.session.rollback()
                raise exception

        ...

    def get_contatos(self, contatos):
        with DbConnectionHandler() as database:
            try:

                stmt = select(contatos).order_by(contatos.id_contatos)
                objects = database.session.scalars(stmt).all()
                print(objects)




            except Exception as exception:
                database.session.rollback()
                raise exception

    def delete_contato(self, tb_contatos, id_):
        with DbConnectionHandler() as database:
            try:

                database.session.execute(
                    delete(tb_contatos).where(tb_contatos.id_contatos == id_)
                )

                database.session.flush()
                database.session.commit()


            except Exception as exception:
                database.session.rollback()
                raise exception
        ...

    def select_contato(self):
        with DbConnectionHandler() as database:
            try:

                stmt = text(f"SELECT id_contatos, nome_contato, telefone, id_cliente, email from contatos;")
                ob = database.session.execute(stmt).fetchall()
                for obs in ob:
                    print(f'(Nome contato = {obs.nome_contato}, '
                          f'Telefone = {obs.telefone}, Email = {obs.email},'
                          f' ID_cliente = {obs.id_cliente})')




            except Exception as exception:
                database.session.rollback()
                raise exception
