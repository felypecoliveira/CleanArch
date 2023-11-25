from src.usecase.interfaces.clientes.delete_cliente_interface import InterfaceDeleteCliente
from src.infra.repository.interfaces.clientes_repository_interface import ClientesRepositoryInterface
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError


class DeleteCliente(InterfaceDeleteCliente):
    def __init__(self, cliente_repository: ClientesRepositoryInterface):
        self.cliente_repository = cliente_repository

    def delete_cliente(self, id_) -> bool:
        try:
            self.validate_id_cliente(id_)
            confirm = self.cliente_repository.confirm_id_cliente(id_)
            if confirm:
                response = self.cliente_repository.delete_cliente(id_)
                return {
                    'sucess': True,
                    'message': 'delete completed',
                    'reponse': response
                }


        except Exception:
            return {'sucess': False, 'message': HttpUnprocessableEntityError("Id cliente nao encontrado")}

    @classmethod
    def validate_id_cliente(cls, id):
        if type(id) == str:
            raise

        if id <= 0:
            raise

