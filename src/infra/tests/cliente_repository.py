from src.domain.model.clientes import ClientesDominio


class ClientesRespositorySpy:
    def __init__(self) -> None:
        self.insert_user_attributes = {}
        self.select_user_attributes = {}


    def insert_cl_ct(self,nome,telefone,cpf,endereco, data_nascimento):
        self.insert_user_attributes["nome"] = nome
        self.insert_user_attributes["telefone"] = telefone
        self.insert_user_attributes["cpf"] = cpf
        self.insert_user_attributes["endereco"] = endereco
        self.insert_user_attributes["data_nascimento"] = data_nascimento


    def select_cliente_by_name(self,nome):
        self.select_user_attributes["nome"] = nome
        return [
            ClientesDominio(),
            ClientesDominio()
        ]
