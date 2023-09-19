from src.domain.settings.connect_settings import DbConnectionHandler
from src.interfaces.clientes_interface import DbInterfaceClientes
from src.domain.core.clientes_core import Clientes as EntityCliente
from src.domain.core.contatos_core import Contatos as EntityContato
from typing import List
from sqlalchemy import select, delete, update


# logica vai ficar aqui e o databaseactions vai chamar


class ClientesUseCase(DbInterfaceClientes):

    def insert_cliente_contato(self,
                               nome_cliente,
                               telefone_cliente,
                               cpf_cliente,
                               endereco_cliente,
                               data_nascimento_cliente,
                               nome_contato,
                               telefone_contato,
                               email_contato):

        with DbConnectionHandler() as database:
            try:
                cliente_registry = EntityCliente(
                    nome_cliente,
                    telefone_cliente,
                    cpf_cliente,
                    endereco_cliente,
                    data_nascimento_cliente)

                contato_registry = EntityContato(
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

    def get_clientes(self, clientes) -> List[EntityCliente]:
        with DbConnectionHandler() as database:
            try:
                stmt = select(clientes).order_by(clientes.id)
                objetos = database.session.scalars(stmt).all()
                print(objetos)

            except Exception as exception:
                database.session.rollback()
                raise exception

    def get_clientes_contatos(self, clientes, contatos) -> List[EntityContato]:

        with DbConnectionHandler() as database:
            try:
                stmt = select(clientes, contatos).join(clientes.contatos) \
                    .order_by(clientes.id, contatos.id_contatos)

                for row in database.session.execute(stmt):
                    print(f"{row}")


            except Exception as exception:
                database.session.rollback()
                raise exception

    def delete_cliente(self, tb_clientes, id_) -> bool:
        with DbConnectionHandler() as database:
            try:
                ...
                database.session.execute(
                    delete(tb_clientes).where(tb_clientes.id == id_)
                )

                database.session.flush()
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def update_cliente(self, id_, clientes, column, update_) -> bool:
        with DbConnectionHandler() as database:
            try:
                database.session.execute(
                    update(clientes),
                    [
                        {"id": id_, column: update_}
                    ]
                )

                database.session.commit()

            except Exception as exception:
                database.session.rollback()
                raise exception
