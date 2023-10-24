from src.interfaces.select_contato import InterfaceSelectContato
from src.main.interfaces.contatos_repository_interface import ContatosRepositoryInterface
from src.domain.infra.model.contatos import ContatosDominio
from typing import List


class SelectContato(InterfaceSelectContato):
    # ID do cliente para verificar sua lista
    # de contatos
    def __init__(self, contatos_repository: ContatosRepositoryInterface):
        self.contatos_repository = contatos_repository

    def select_contato(self, id_) -> List[ContatosDominio]:
        try:
            response = self.contatos_repository.select_contato(id_)


            return {
                'sucess': True,
                'message': response
            }

        except Exception as exception:
            return {
                'sucess': False,
                'detail': exception
            }



