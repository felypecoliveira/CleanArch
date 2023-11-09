from src.interfaces.contatos.delete_contato_interface import InterfaceDeleteContato
from src.infra.repository.interfaces.contatos_repository_interface import ContatosRepositoryInterface
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError


class DeleteContatos(InterfaceDeleteContato):
    def __init__(self, contatos_repository: ContatosRepositoryInterface):
        self.contatos_repository = contatos_repository

    def delete_contato(self, id_: int) -> bool:
        try:
            confirm = self.contatos_repository.confirm_id_contato(id_)
            if confirm:
                response = self.contatos_repository.delete_contato(id_)
                return {'sucess': True, 'message': 'delete completed'}

        except Exception as exception:
            return {'sucess': False, 'message': HttpUnprocessableEntityError("Id contato nao encontrado")}
