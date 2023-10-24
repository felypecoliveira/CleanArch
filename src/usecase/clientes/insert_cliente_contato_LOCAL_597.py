from src.main.interfaces.clientes_repository_interface import ClientesRepositoryInterface
from src.interfaces.insert_cliente_contato import InterfaceClienteContato
from src.domain.infra.model.clientes import ClientesDominio
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
                               email_contato: str) -> ClientesDominio:

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

            return {

                "sucess": True, "attributes": {
                    "nome":nome,
                    "telefone":telefone,
                    "cpf":cpf,
                    "endereco":endereco,
                    "data_nascimento":data_nascimento,
                    "nome_contato":nome_contato,
                    "telefone_contato":telefone_contato,
                    "email":email_contato},

                "type": "clientes_contatos"
            }

        except Exception as error:
            return {'sucess': False, 'detail': error}

