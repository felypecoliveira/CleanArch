from src.interfaces.contatos.update_contato import InterfaceUpdateContatos
from src.main.interfaces.contatos_repository_interface import ContatosRepositoryInterface


class UpdateContatos(InterfaceUpdateContatos):
    def __init__(self, contatos_repository: ContatosRepositoryInterface):
        self.contatos_repository = contatos_repository

    def update_contato(self, id_, column, update_):

        try:
            response = self.contatos_repository.update_contato(id_, column, update_)


            return {
                'sucess': True,
                'message': "update sucessfully completed"
            }

        except Exception as exception:
            return {
                'sucess': False,
                'detail': exception
            }



