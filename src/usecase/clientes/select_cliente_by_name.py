from src.interfaces.clientes.select_cliente_by_name_interface import InterfaceSelectClienteByName
from src.infra.repository.interfaces.clientes_repository_interface import ClientesRepositoryInterface
from src.domain.entities.clientes import Clientes as DomainClientes
from src.errors.types.http_bad_request import HttpBadRequestError
import re


class SelectClienteName(InterfaceSelectClienteByName):
    def __init__(self, cliente_repository: ClientesRepositoryInterface):
        self.cliente_repository = cliente_repository

    def select_cliente_by_name(self, name: str) -> DomainClientes:
        response = self.cliente_repository.select_cliente_by_name(name)
        self.__valid_name(name)

        try:
            if response:
                return {
                    'sucess': True,
                    'message': response}





        except Exception as error:
            return {
                'sucess': False,
                'message': HttpBadRequestError(error)
            }

    @classmethod
    def __valid_name(cls, nome):
        find_numbers = [n for n in nome if n in "0123456789"]
        especial = re.match(r'^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$', nome)
        if 1 <= len(nome) >= 50:
            raise HttpBadRequestError("Nome muito curto ou muito longo, tente novamente")

        if find_numbers:
            raise HttpBadRequestError("Nome nao  pode conter numero(s)")

        if not especial:
            raise HttpBadRequestError("Nome não conter caracteres especiais")

        return nome
