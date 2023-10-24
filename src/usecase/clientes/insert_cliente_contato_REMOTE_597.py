from src.main.interfaces.clientes_repository_interface import ClientesRepositoryInterface
from src.interfaces.insert_cliente_contato import InterfaceClienteContato
from src.domain.repository.clientes_repository import ClientesRepository
from src.domain.models.clientes import Clientes
from datetime import date


class InsertClienteContato(InterfaceClienteContato):
    def __init__(self, cliente_repository: ClientesRepositoryInterface):
        self.cliente_repository = cliente_repository

    def insert_cliente_contato(self,
                               nome: str,
                               telefone: str,
                               cpf: str,
                               endereco: str,
                               data_nascimento: date,
                               nome_contato: str,
                               telefone_contato: str,
                               email_contato: str) -> Clientes:

        try:
            self.cliente_repository.insert_cliente_contato(
                nome,
                telefone,
                cpf,
                endereco,
                data_nascimento,
                nome_contato,
                telefone_contato,
                email_contato,
            )

            return {'sucess': True, 'message': 'insert realizado'}

        except Exception as error:
            return {'sucess': False, 'message': error}

