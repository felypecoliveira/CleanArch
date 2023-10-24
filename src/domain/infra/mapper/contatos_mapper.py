from src.domain.entities.contatos import Contatos as EntityContatos
from src.domain.infra.model.contatos import ContatosDominio


class ContatosMapper:

    @classmethod
    def to_domain(cls, json_to_domain):
        try:
            contatos_dominio = ContatosDominio(id_contatos=None,
                                               nome_contato=json_to_domain['nome_contato'],
                                               telefone=json_to_domain['telefone'],
                                               email=json_to_domain['email'],
                                               id_cliente=None)
            
            return contatos_dominio
        except:
            raise Exception("Algo de errado ocorreu revise o arquivo json e tente novamente")

    @classmethod
    def to_data(cls, json_to_data):
        try:
            contatos_data = EntityContatos(nome_contato=json_to_data['nome_contato'],
                                           telefone=json_to_data['telefone'],
                                           email=json_to_data['email']
                                           )
        except:
            raise Exception("Algo de errado ocorreu revise o arquivo json e tente novamente")

