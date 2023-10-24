from src.interfaces.addcontato_to_cliente import InterfaceContatoCliente
from src.main.interfaces.contatos_repository_interface import ContatosRepositoryInterface


class AddContatoCliente(InterfaceContatoCliente):
    def __init__(self, contatos_repository: ContatosRepositoryInterface):
        self.contatos_repository = contatos_repository

    def add_contato_to_cliente(self,
                               id,
                               nome_contato,
                               telefone,
                               email):
        try:
            self.contatos_repository.add_contato_to_cliente(
                id,
                nome_contato,
                telefone,
                email
            )

            return {
                "sucess":True, "attributes":{
                    "nome_contato":nome_contato,
                    "telefone_contato":telefone,
                    "email":email,
                    "id_cliente":id
                },
                "type": "contatos_clientes"
                }

        except Exception as error:
            return {'sucess': False, 'message': error}

