from src.usecase.interfaces.clientes.get_clientes_contatos_interface import InterfaceGetClientesContatos
from src.infra.repository.interfaces.clientes_repository_interface import ClientesRepositoryInterface
from src.domain.model.contatos import ContatosDominio
from typing import List


class GetClientesContatos(InterfaceGetClientesContatos):
    def __init__(self, cliente_repository: ClientesRepositoryInterface):
        self.cliente_repository = cliente_repository

    def get_clientes_contatos(self) -> List[ContatosDominio]:
        try:
            response = self.cliente_repository.get_clientes_contatos()

            return {'sucess': True, 'message': response}

        except Exception as error:
            return {'sucess': False, 'message': error}





