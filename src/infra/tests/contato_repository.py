from typing import List
from src.domain.model.contatos import ContatosDominio


class ContatosRepositorySpy:
    def __init__(self) -> None:
        self.insert_ct_attributes = {}
        self.select_ct_atrributes = {}


    def insert_ct(self,id_cliente, nome, telefone, email) -> ContatosDominio:
        ...


    def select_contato(self,id) -> List[ContatosDominio]:
        ...