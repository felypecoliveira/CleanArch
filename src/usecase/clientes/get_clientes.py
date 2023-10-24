from src.main.interfaces.clientes_repository_interface import ClientesRepositoryInterface
from src.interfaces.get_clientes import InterfaceGetCliente
from src.domain.entities.clientes import Clientes
from typing import List


class GetClientes(InterfaceGetCliente):
    def __init__(self, cliente_repository: ClientesRepositoryInterface):
        self.cliente_repository = cliente_repository

    def get_clientes(self) -> List[Clientes]:

        try:
            response = self.cliente_repository.get_clientes()

            return {
                'sucess': True,
                'message': response
            }
        except Exception as error:
            return {
                'sucess': False,
                'detail': error
            }



