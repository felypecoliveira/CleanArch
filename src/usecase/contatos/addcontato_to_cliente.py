from src.interfaces.contatos.addcontato_to_cliente_interface import InterfaceContatoCliente
from src.infra.repository.interfaces.contatos_repository_interface import ContatosRepositoryInterface
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError
import re


class AddContatoCliente(InterfaceContatoCliente):
    def __init__(self, contatos_repository: ContatosRepositoryInterface):
        self.contatos_repository = contatos_repository

    def add_contato_to_cliente(self,
                               id,
                               nome_contato,
                               telefone,
                               email):
        try:
            self.__validate_nome_contato(nome_contato)
            self.__validate_telefone_contato(telefone)
            self.__validate_email_contato(email)

            self.contatos_repository.add_contato_to_cliente(
                id,nome_contato,telefone,email
            )

            return {
                "sucess": True, "attributes": {
                    "nome_contato": nome_contato,
                    "telefone_contato": telefone,
                    "email": email,
                    "id_cliente": id
                },
                "type": "contato_do_cliente"
            }

        except Exception as error:
            return {'sucess': False, 'message': error}

    @classmethod
    def __validate_nome_contato(cls, nome):
        find_numbers = [n for n in nome if n in "0123456789"]
        especial = re.match(r'^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$', nome)
        if 1 <= len(nome) >= 50:
            raise HttpUnprocessableEntityError("Nome muito longo ou muito curto")

        if find_numbers:
            raise HttpUnprocessableEntityError("Nome nao pode conter numeros")

        if not especial:
            raise HttpUnprocessableEntityError("Nome nao pode conter caracteres especiais")

    @classmethod
    def __validate_telefone_contato(cls,telefone):
        regex = r"^\d{2}0?\d{9}$"
        if re.match(regex, telefone):
            if all(char == telefone[0] for char in telefone):
                raise HttpUnprocessableEntityError("Todos os numeros sao iguais, formato invalido. ")
            return telefone
        else:
            raise HttpUnprocessableEntityError("Numero de telefone invalido")


    @classmethod
    def __validate_email_contato(cls,email):
        regex = re.compile(r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+"
                           r"/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:"
                           r"[a-z0-9-]*[a-z0-9])?$")

        if re.fullmatch(regex, email):
            return True
        else:
            raise HttpUnprocessableEntityError("Email invalido, insira um endereco valido")
