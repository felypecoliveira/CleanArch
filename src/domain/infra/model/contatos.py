from pydantic import (BaseModel,
                      StrictInt,
                      StrictStr,
                      field_validator)

import re


class ContatosDominio(BaseModel):
    id_contatos: StrictInt = None
    nome_contato: StrictStr
    telefone: str
    email: str
    id_cliente: StrictInt = None

    @field_validator('nome_contato')
    def validate_nome_contato(cls, nome_ct):
        find_numbers = [n for n in nome_ct if n in "0123456789"]
        especial = re.match(r'^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$', nome_ct)
        if 1 <= len(nome_ct) >= 50:
            raise ValueError("Nome muito curto ou muito longo, tente novamente")

        if find_numbers:
            raise ValueError("Nome não pode conter nº(s)")

        if not especial:
            raise ValueError("Nome não conter caracteres especiais")

        return nome_ct

    @field_validator('telefone')
    def validate_telefone_contato(cls, telefone):
        regex = r"^\d{2}0?\d{9}$"
        if re.match(regex, telefone):
            if all(char == telefone[0] for char in telefone):
                raise ValueError("Todos os numeros são iguais, formato invalido. ")
            return telefone
        else:
            raise ValueError("Número de telefone invalido")

    @field_validator('email')
    def validate_email(cls, email):
        regex = re.compile(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@"
                           r"[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")
        if re.fullmatch(regex, email):
            return email
        else:
            raise ValueError("Formato de email invalido insira novamente")

