from datetime import date


class ClientesDominio:
    def __init__(self,
                 id: int,
                 nome: str,
                 telefone: str,
                 cpf: str,
                 endereco: str,
                 data_nascimento: date):
        self.__id = id
        self.__nome = nome
        self.__telefone = telefone
        self.__cpf = cpf
        self.__endereco = endereco
        self.__data_nascimento = data_nascimento

    @property
    def nome(self): return self.__nome

    @nome.setter
    def nome(self, valor): self.__nome = valor

    @property
    def telefone(self): return self.__telefone

    @telefone.setter
    def telefone(self, valor): self.__telefone = valor

    @property
    def cpf(self): return self.__cpf

    @cpf.setter
    def cpf(self, valor): self.__cpf = valor

    @property
    def endereco(self): return self.__cpf

    @endereco.setter
    def endereco(self, valor): self.__endereco = valor

    @property
    def data_nascimento(self): return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, valor): self.__data_nascimento = valor

    def __repr__(self) -> str:
        return f"Cliente < ID = {self.__id}, Nome completo = {self.__nome};"\
               f"Telefone = {self.__telefone};"\
               f"CPF = {self.__cpf};"\
               f"Endereco = {self.__endereco};"\
               f"Data de nascimento = {self.__data_nascimento}>"\

