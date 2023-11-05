from src.main.interfaces.contatos_repository_interface import ContatosRepositoryInterface
from src.interfaces.contatos.get_contatos_interface import InterfaceGetContatos
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError


class GetContatos(InterfaceGetContatos):
    def __init__(self, contatos_repository: ContatosRepositoryInterface):
        self.contatos_repository = contatos_repository

    def get_contatos(self):

        try:
            response = self.contatos_repository.get_contatos()

            return {
                'sucess': True,
                'message': response
            }
        except Exception as error:
            return {
                'sucess': False,
                'detail': HttpUnprocessableEntityError(error)
            }




