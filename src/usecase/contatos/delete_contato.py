from src.interfaces.contatos.delete_contato import InterfaceDeleteContato
from src.main.interfaces.contatos_repository_interface import ContatosRepositoryInterface


class DeleteContatos(InterfaceDeleteContato):
    def __init__(self, contatos_repository: ContatosRepositoryInterface):
        self.contatos_repository = contatos_repository

    def delete_contato(self, id_: int) -> bool:
        try:
            self.contatos_repository.delete_contato(id_)

            return {'sucess':True, 'message': 'delete completed'}

        except Exception as exception:
            return {'sucess':False, 'message': exception}

