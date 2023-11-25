class ContatosDominio:
    def __init__(self, id_contatos: int, nome_contato: str, telefone_contato: str, email: str, id_cliente: int):
        self.__id_contatos = id_contatos
        self.__nome_contato = nome_contato
        self.__telefone_contato = telefone_contato
        self.__email = email
        self.__id_cliente = id_cliente

    @property
    def nome_contato(self): return self.__nome_contato

    @nome_contato.setter
    def nome_contato(self, valor): self.__nome_contato = valor

    @property
    def telefone_contato(self): return self.__telefone_contato

    @telefone_contato.setter
    def telefone_contato(self, valor): self.__telefone_contato = valor

    @property
    def email(self): return self.__email

    @email.setter
    def email(self, valor): self.__email = valor

    def __repr__(self) -> str:
        return f"Contato < id_contatos = {self.__id_contatos}, " \
               f"\nnome_contato = {self.__nome_contato};" \
               f" \ntelefone_contato = {self.__telefone_contato};" \
               f" \nemail = {self.__email}>" \
               f"\nfk_cliente = {self.__id_cliente}"
