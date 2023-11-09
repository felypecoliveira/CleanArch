from src.interfaces.contatos.update_contato_interface import InterfaceUpdateContatos
from src.infra.repository.interfaces.contatos_repository_interface import ContatosRepositoryInterface
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError
import re


class UpdateContatos(InterfaceUpdateContatos):
    def __init__(self, contatos_repository: ContatosRepositoryInterface):
        self.contatos_repository = contatos_repository

    def update_contato(self, id_,
                       column,
                       update_):

        try:
            if column == "nome_contato":
                nome_contato = self.__validate_nome_contato_update(update_)

            elif column == "telefone_contato":
                telefone_contato = self.__validate_telefone_contato_update(update_)

            elif column == "email":
                email = self.__validate_email_contato_update(update_)

            else:
                raise HttpUnprocessableEntityError("Campo invalido")


            self.contatos_repository.update_contato(id_, column, update_)

            return {'sucess': True, 'message': "update completed sucessfully "}


        except Exception as error:
            return {
                'sucess': False,
                'message': error
            }

    @classmethod
    def __validate_nome_contato_update(cls, nome):
        find_numbers = [n for n in nome if n in "0123456789"]
        especial = re.match(r'^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$', nome)
        if 1 <= len(nome) >= 50:
            raise HttpUnprocessableEntityError("Nome muito longo ou muito curto")

        if find_numbers:
            raise HttpUnprocessableEntityError("Nome nao pode conter numeros")

        if not especial:
            raise HttpUnprocessableEntityError("Nome nao pode conter caracteres especiais")

    @classmethod
    def __validate_telefone_contato_update(cls, telefone):
        regex = r"^\d{2}0?\d{9}$"
        if re.match(regex, telefone):
            if all(char == telefone[0] for char in telefone):
                raise HttpUnprocessableEntityError("Todos os numeros sao iguais, formato invalido. ")
            return telefone
        else:
            raise HttpUnprocessableEntityError("Numero de telefone invalido")

    @classmethod
    def __validate_email_contato_update(cls, email):
        regex = re.compile(r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+"
                           r"/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:"
                           r"[a-z0-9-]*[a-z0-9])?$")

        if re.fullmatch(regex, email):
            return True
        else:
            raise HttpUnprocessableEntityError("Email invalido, insira um endereco valido")
