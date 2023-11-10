class ContatosDominio:
    def __init__(self, id_contatos: int, nome_contato: str, telefone_contato: str, email: str, id_cliente: int):
        self.id_contatos = id_contatos
        self.nome_contato = nome_contato
        self.telefone_contato = telefone_contato
        self.email = email
        self.id_cliente = id_cliente
