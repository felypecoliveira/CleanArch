from src.infra.tests.f_tests import __random_phone_numbers, __random_id
from src.domain.model.contatos import ContatosDominio
from typing import List
from faker import Faker

fake = Faker("pt_BR")
random_name = fake.name()
random_telefone = __random_phone_numbers()
random_email = fake.email()
id_fk_cliente = __random_id()
id_contatos = __random_id()


class ContatosRepositorySpy:
    def __init__(self):
        self.insert = {}
        self.select = {}

    # Create
    def add_contato_to_cliente(self, id_cliente, nome, telefone, email) -> ContatosDominio:
        self.insert["id_cliente"] = id_cliente
        self.insert["nome_contato"] = nome
        self.insert["telefone_contato"] = telefone
        self.insert["email"] = email

    # Aqui seleciona um id de cliente  e mostra quantos contatos
    # esse cliente possui
    def select_contato(self, id_cliente) -> List[ContatosDominio]:
        self.select["id_cliente"] = id_cliente
        return [
            ContatosDominio(id_contatos,
                            random_name,
                            random_telefone,
                            random_email,
                            id_cliente)
        ]

    # Update
    def update_contato(self, id: int, column: str, update: str):
        if column == "nome_contato":
            post = self.__select_contato_by_id(id).nome_contato = update
            return ContatosDominio(id,
                                   post,
                                   random_telefone,
                                   random_email,
                                   id_fk_cliente)

        elif column == "telefone_contato":
            post = self.__select_contato_by_id(id).telefone_contato = update
            return ContatosDominio(id,
                                   random_name,
                                   post,
                                   random_email,
                                   id_fk_cliente)

        elif column == "email":
            post = self.__select_contato_by_id(id).email
            return ContatosDominio(id,
                                   random_name,
                                   random_telefone,
                                   post,
                                   id_fk_cliente)

    def delete_contato(self, id_contato: int):
        post = self.__select_contato_by_id(id_contato)
        del post

    def confirm_id_contato(self, id: int):
        contatos = self.__select_contato_by_id(id)
        return contatos

    def __select_contato_by_id(self, id_contato: int) -> ContatosDominio:
        self.select["id_contato"] = id_contato
        return ContatosDominio(id_contato,
                               random_name,
                               random_telefone,
                               random_email,
                               id_fk_cliente)
