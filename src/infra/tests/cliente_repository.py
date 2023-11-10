from src.domain.model.clientes import ClientesDominio as Clientes
from typing import List


class ClientesRespositorySpy:
    def __init__(self) -> None:
        self.insert_user_attributes = {}
        self.select_clientes_attributes = {}

    def insert_cl_ct(self, nome, telefone, cpf, endereco, data_nascimento):
        self.insert_user_attributes["nome"] = nome
        self.insert_user_attributes["telefone"] = telefone
        self.insert_user_attributes["cpf"] = cpf
        self.insert_user_attributes["endereco"] = endereco
        self.insert_user_attributes["data_nascimento"] = data_nascimento

    def select_cliente_by_name(self, nome) -> List[Clientes]:
        self.select_clientes_attributes["nome"] = nome
        return [
            Clientes(44, nome, "62985785227", "05110918180", "Av janizeiro ribeiro", "1998-08-31"),
            Clientes(44, nome, "62985582078", "70016927192", "Jaques Russuau", "1989-05-12")
        ]
