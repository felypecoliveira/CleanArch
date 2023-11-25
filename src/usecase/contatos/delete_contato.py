from src.usecase.interfaces.contatos.delete_contato_interface import InterfaceDeleteContato
from src.infra.repository.interfaces.contatos_repository_interface import ContatosRepositoryInterface
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError


class DeleteContatos(InterfaceDeleteContato):
    def __init__(self, contatos_repository: ContatosRepositoryInterface):
        self.contatos_repository = contatos_repository

    def delete_contato(self, id_: int) -> bool:
        try:
            self.__validate_id_contato(id_)
            confirm = self.contatos_repository.confirm_id_contato(id_)
            if confirm:
                response = self.contatos_repository.delete_contato(id_)
                return {'sucess': True,
                        'message': 'delete completed',
                        'response': response}

        except Exception:
            return {'sucess': False, 'message': HttpUnprocessableEntityError("Id contato nao encontrado")}


    @classmethod
    def __validate_id_contato(cls, id):
        if type(id) == str:
            raise

        if id <= 0:
            raise
