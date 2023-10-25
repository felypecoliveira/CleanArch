from src.interfaces.clientes.delete_cliente import InterfaceDeleteCliente
from src.main.interfaces.clientes_repository_interface import ClientesRepositoryInterface


class DeleteCliente(InterfaceDeleteCliente):
    def __init__(self, cliente_repository: ClientesRepositoryInterface):
        self.cliente_repository = cliente_repository

    def delete_cliente(self, id_) -> bool:
        try:
            self.cliente_repository.delete_cliente(id_)

            return {'sucess':True, 'message': 'delete completed'}



        except Exception as exception:
            return {'sucess': False, 'message': exception}

