from pydantic import (BaseModel,
                      StrictInt,
                      StrictStr,
                      field_validator)
from datetime import date
import re


class ClientesDominio(BaseModel):
    id: StrictInt = None
    nome: StrictStr
    telefone: str
    cpf: str
    endereco: StrictStr
    data_nascimento: date

    @field_validator('nome')
    def valid_name(cls, nome):
        find_numbers = [n for n in nome if n in "0123456789"]
        especial = re.match(r'^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$', nome)
        if 1 <= len(nome) >= 50:
            raise ValueError("Nome muito curto ou muito longo, tente novamente")

        if find_numbers:
            raise ValueError("Nome não pode conter nº(s)")

        if not especial:
            raise ValueError("Nome não conter caracteres especiais")

        return nome

    @field_validator('telefone')
    def validate_telefone(cls, telefone):
        regex = r"^\d{2}0?\d{9}$"
        if re.match(regex, telefone):
            if all(char == telefone[0] for char in telefone):
                raise ValueError("Todos os numeros são iguais, formato invalido. ")
            return telefone
        else:
            raise ValueError("Número de telefone invalido")

    @field_validator('cpf')
    def validate_cpf(cls, cpf):
        cpf = cpf.replace(".", "").replace("-", "")
        if not cpf.isdigit():
            raise ValueError("CPF invalido, deve conter apenas números")

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
            raise ValueError("CPF invalido há menos de 11 digitos.")

        # Verificando se todos os numeros sao iguais
        if all(char == cpf[0] for char in cpf):
            raise ValueError("CPF invalido todos os números são iguais")

        if cpf == cpf_11_digit:
            return cpf
        else:
            raise ValueError("CPF não esta de acordo com a estrutura basica")


