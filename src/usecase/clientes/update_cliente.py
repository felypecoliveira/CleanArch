from src.interfaces.clientes.update_cliente_interface import InterfaceUpdateCliente
from src.domain.interfaces.clientes_repository_interface import ClientesRepositoryInterface
import datetime
from datetime import date
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError
import re


class UpdateCliente(InterfaceUpdateCliente):
    def __init__(self, cliente_repository: ClientesRepositoryInterface):
        self.cliente_repository = cliente_repository

    def update_cliente(self,
                       id_: int,
                       column: str,
                       update_: str | date) -> bool:
        try:
            if column == "nome":
                nome = self.__validate_nome_cliente_update(update_)

            if column == "telefone":
                telefone = self.__validate_telefone_cliente_update(update_)

            if column == "cpf":
                cpf = self.__validate_cpf_cliente_update(update_)

            if column == "data_nascimento":
                data = self.__validate_data_nascimento_cliente_update(update_)

            else:
                raise HttpUnprocessableEntityError("Campo invalido")



            response = self.cliente_repository.update_cliente(id_, column, update_)

            return {'sucess': True, 'message': "update completed sucessfully "}



        except Exception as error:
            return {
                'sucess': False,
                'message': error
            }


    @classmethod
    def __validate_nome_cliente_update(cls, nome):
        find_numbers = [n for n in nome if n in "0123456789"]
        especial = re.match(r'^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$', nome)
        if 1 <= len(nome) >= 50:
            raise HttpUnprocessableEntityError("Nome muito longo insira um nome menor, abrevie se necessario ")

        if find_numbers:
            raise HttpUnprocessableEntityError("Nome nao pode conter numeros")

        if not especial:
            raise HttpUnprocessableEntityError("Nome nao pode conter caracteres especiais")

    @classmethod
    def __validate_telefone_cliente_update(cls, telefone):
        regex = r"^\d{2}0?\d{9}$"
        if re.match(regex, telefone):
            if all(char == telefone[0] for char in telefone):
                raise HttpUnprocessableEntityError("Todos os numeros sao iguais, formato invalido. ")
            return telefone
        else:
            raise HttpUnprocessableEntityError("Numero de telefone invalido")

    @classmethod
    def __validate_cpf_cliente_update(cls, cpf):
        cpf = cpf.replace(".", "").replace("-", "")
        if not cpf.isdigit():
            raise HttpUnprocessableEntityError("CPF invalido, deve conter apenas números")

        cpf_9_digit = cpf[:-2]
        # Calculando o primeiro digito verificador
        somado = 0
        down_count = 11
        for c in cpf_9_digit:
            c = int(c)
            down_count -= 1
            somando = down_count * c
            somado += somando

        vd1 = 0 if (somado % 11) < 2 else (11 - somado % 11)
        cpf_10_digit = str(cpf_9_digit) + str(vd1)

        # Calculando o segundo digito verificador
        somado = 0
        down_count = 12
        for c in cpf_10_digit:
            down_count -= 1
            somando = int(c) * down_count
            somado += somando

        vd2 = 0 if (somado % 11) < 2 else (11 - somado % 11)
        cpf_11_digit = str(cpf_10_digit) + str(vd2)

        # Verificando se o cpf tem menos de 11 digitos
        if len(cpf) < 11 or len(cpf) > 11:
            raise HttpUnprocessableEntityError("CPF invalido há menos de 11 digitos.")

        # Verificando se todos os numeros sao iguais
        if all(char == cpf[0] for char in cpf):
            raise HttpUnprocessableEntityError("CPF invalido todos os números sao iguais")

        if cpf == cpf_11_digit:
            return cpf
        else:
            raise HttpUnprocessableEntityError("CPF nao esta de acordo com a estrutura basica")

    @classmethod
    def __validate_data_nascimento_cliente_update(cls, data):
        try:
            datetime.datetime.strptime(data, "%Y-%m-%d")
            return True
        except Exception as exception:
            raise HttpUnprocessableEntityError("Formato de data invalido, insira a data corretamente")
