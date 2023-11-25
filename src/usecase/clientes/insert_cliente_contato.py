from src.infra.repository.interfaces.clientes_repository_interface import ClientesRepositoryInterface
from src.usecase.interfaces.clientes.insert_cliente_contato_interface import InterfaceClienteContato
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError
from src.domain.model.clientes import ClientesDominio
from datetime import datetime
import re


class InsertClienteContato(InterfaceClienteContato):
    def __init__(self, cliente_repository: ClientesRepositoryInterface):
        self.cliente_repository = cliente_repository

    def insert_cliente_contato(self,
                               nome: str,
                               telefone: str,
                               cpf: str,
                               endereco: str,
                               data_nascimento: str,
                               nome_contato: str,
                               telefone_contato: str,
                               email_contato: str) -> ClientesDominio:

        try:
            self.__valid_name(nome)
            self.__validate_telefone(telefone)
            self.__validate_cpf(cpf)
            self.__validate_date(data_nascimento)
            self.__valid_name(nome_contato)
            self.__validate_telefone(telefone_contato)
            self.__validate_email(email_contato)

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
                    "nome": nome,
                    "telefone": telefone,
                    "cpf": cpf,
                    "endereco": endereco,
                    "data_nascimento": data_nascimento,
                    "nome_contato": nome_contato,
                    "telefone_contato": telefone_contato,
                    "email": email_contato},
                "type": "clientes_contatos"
            }



        except Exception as error:
            return {'sucess': False, 'message': HttpUnprocessableEntityError(error)}

    @classmethod
    def __valid_name(cls, nome):
        find_numbers = [n for n in nome if n in "0123456789"]
        especial = re.match(r'^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$', nome)
        sequencia = ""

        if sequencia:
            ...

        if len(nome) < 1 or len(nome) == 1 or  len(nome) > 50 or len(nome) == 50:
            raise HttpUnprocessableEntityError("Nome muito curto ou muito longo, tente novamente")

        if find_numbers:
            raise HttpUnprocessableEntityError("Nome nao pode conter nº(s)")

        if not especial:
            raise HttpUnprocessableEntityError("Nome nao conter caracteres especiais")

        return nome

    @classmethod
    def __validate_telefone(cls, telefone):
        regex = r"^\d{2}0?\d{9}$"
        if re.match(regex, telefone):
            if all(char == telefone[0] for char in telefone):
                raise HttpUnprocessableEntityError("Todos os numeros sao iguais, formato invalido. ")
            return telefone
        else:
            raise HttpUnprocessableEntityError("Numero de telefone invalido")

    @classmethod
    def __validate_cpf(cls, cpf):
        especiais = "-!@#$%¨&*()+:;|\/*."
        if not re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf):
            raise HttpUnprocessableEntityError("CPF está no formato incorreto")

        for cpfs in cpf:
            if cpfs in especiais:
                raise HttpUnprocessableEntityError("Digite apenas os numeros do cpf")

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
            raise HttpUnprocessableEntityError("CPF nao esta de acordo com a estrutura padrao")

    @classmethod
    def __validate_date(cls, date_):
        try:
            if datetime.strptime(date_, "%Y-%m-%d"):
                return True

        except:
            raise HttpUnprocessableEntityError("Formato de data invalido insira yyyy-mm-dd")

    @classmethod
    def __validate_email(cls, email):
        # Define uma expressão regular para validar e-mails
        email_pattern = r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:" \
                        r"[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$"

        if re.match(email_pattern, email):
            return True
        else:
            raise HttpUnprocessableEntityError("Formato de email invalido tente novamente")
