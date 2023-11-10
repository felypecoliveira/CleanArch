from datetime import date


class ClientesDominio:
    def __init__(self, id: int, nome: str, telefone: str, cpf: str, endereco: str, data_nascimento: date):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.endereco = endereco
        self.data_nascimento = data_nascimento
