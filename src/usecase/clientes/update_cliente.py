from src.interfaces.update_cliente import InterfaceUpdateCliente
from src.main.interfaces.clientes_repository_interface import ClientesRepositoryInterface
from src.domain.repository.clientes_repository import ClientesRepository
from datetime import date


class UpdateCliente(InterfaceUpdateCliente):
    def __init__(self, cliente_repository: ClientesRepositoryInterface):
        self.cliente_repository = cliente_repository

    def update_cliente(self,
                       id_: int,
                       column: str,
                       update_: str | date) -> bool:
        try:
            response = self.cliente_repository.update_cliente(id_,
                                                              column,
                                                              update_)

            return {'sucess': True, 'message': "update completed sucessfully "}



        except Exception as error:
            return {
                'sucess': False,
                'message': error
            }

