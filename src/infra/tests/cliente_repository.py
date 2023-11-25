from src.domain.model.clientes import ClientesDominio
from src.infra.tests.f_tests import __random_phone_numbers
from faker import Faker
from typing import List

fake = Faker("pt_BR")
random_name = fake.name()
random_telefone = __random_phone_numbers()
random_cpf = fake.cpf()
random_address = fake.address()
random_data = fake.date_of_birth(minimum_age=20, maximum_age=85)


class ClientesRespositorySpy:
    def __init__(self) -> None:
        self.insert = {}
        self.select = {}

    # Create
    def insert_cliente_contato(self,
                               nome,
                               telefone,
                               cpf,
                               endereco,
                               data_nascimento,
                               nome_contato,
                               telefone_contato,
                               email):

        # Clientes attrs
        self.insert["nome"] = nome
        self.insert["telefone"] = telefone
        self.insert["cpf"] = cpf
        self.insert["endereco"] = endereco
        self.insert["data_nascimento"] = data_nascimento

        # Contatos attrs
        self.insert["nome_contato"] = nome_contato
        self.insert["telefone_contato"] = telefone_contato
        self.insert["email"] = email

    # Read
    def select_cliente_by_name(self, nome_) -> List[ClientesDominio]:
        self.select["nome"] = nome_
        return [
            ClientesDominio(44, nome_, "62985785227", "05110918180", "Av janizeiro ribeiro", "1998-08-31"),
        ]

    def __select_cliente_by_id(self, id: int) -> ClientesDominio:
        self.select["id"] = id
        return ClientesDominio(id,
                               random_name,
                               random_telefone,
                               random_cpf,
                               random_address,
                               random_data)

    # Update
    def update_cliente(self, id, column, update):
        if column == "nome":
            post = self.__select_cliente_by_id(id).nome = update
            return ClientesDominio(id,
                                   post,
                                   random_telefone,
                                   random_cpf,
                                   random_address,
                                   random_data)
        elif column == "telefone":
            post = self.__select_cliente_by_id(id).telefone = update
            return ClientesDominio(id,
                                   random_name,
                                   post,
                                   random_cpf,
                                   random_address,
                                   random_data)


        elif column == "cpf":
            post = self.__select_cliente_by_id(id).cpf = update
            return ClientesDominio(id,
                                   random_name,
                                   random_telefone,
                                   post,
                                   random_address,
                                   random_data)



        elif column == "endereco":
            post = self.__select_cliente_by_id(id).endereco = update
            return ClientesDominio(id,
                                   random_name,
                                   random_telefone,
                                   random_cpf,
                                   post,
                                   random_data)

        elif column == "data_nascimento":
            post = self.__select_cliente_by_id(id).data_nascimento = update
            return ClientesDominio(id,
                                   random_name,
                                   random_telefone,
                                   random_cpf,
                                   random_address,
                                   post)
        else:
            raise ValueError("Valores fornecidos para update estão incorretos")

    # Delete
    def delete_cliente(self, id):
        post = self.__select_cliente_by_id(id)
        del post

    def confirm_id_cliente(self,id):
        cliente = self.__select_cliente_by_id(id)
        return cliente
