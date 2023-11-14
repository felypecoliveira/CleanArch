from src.usecase.interfaces.contatos.select_contato_interface import InterfaceSelectContato
from src.infra.repository.interfaces.contatos_repository_interface import ContatosRepositoryInterface
from src.domain.model.contatos import ContatosDominio
from typing import List


class SelectContato(InterfaceSelectContato):
    # ID do cliente para verificar sua lista
    # de contatos
    def __init__(self, contatos_repository: ContatosRepositoryInterface):
        self.contatos_repository = contatos_repository

    def select_contato(self, id_) -> List[ContatosDominio]:
        try:
            response = self.contatos_repository.select_contato(id_)
            if response is None:
                return {'sucess': False, 'message': "cliente não existe"}

            return {'sucess': True, 'message': response}

        except Exception as error:
            return {
                'sucess': False,
                'message': error
            }
