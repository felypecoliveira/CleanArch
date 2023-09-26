from src.usecase.clientes.insert_cliente_contato import InsertClienteContato
from src.domain.repository.clientes_repository import ClientesRepository


def insert():
    clientes_repository = ClientesRepository()
    inserts = InsertClienteContato(clientes_repository)
    return inserts


insert().insert_cliente_contato('',
                                         '',
                                         '',
                                         '',
                                         '',
                                         '',
                                         '',
                                         '')
