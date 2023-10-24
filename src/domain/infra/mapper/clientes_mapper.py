from src.domain.entities.clientes import Clientes as EntityClientes
from src.domain.infra.model.clientes import ClientesDominio


class ClientesMapper:
    # Recebe um json e esse formato de arquivo é transformado em dominio ou model
    @classmethod
    def to_domain(cls, **json_to_domain):

        try:
            cliente_dominio = ClientesDominio(
                                              nome=json_to_domain['nome'],
                                              telefone=json_to_domain['telefone'],
                                              cpf=json_to_domain['cpf'],
                                              endereco=json_to_domain['endereco'],
                                              data_nascimento=json_to_domain['data_nascimento'])
            return cliente_dominio

        except:
            raise Exception("Algo de errado ocorreu revise o arquivo json e tente novamente")

    @classmethod
    def to_data(cls, **json_to_data):
        try:
            clientes_data = EntityClientes(nome=json_to_data['nome'],
                                           telefone=json_to_data['telefone'],
                                           cpf=json_to_data['cpf'],
                                           endereco=json_to_data['endereco'],
                                           data_nascimento=json_to_data['data_nascimento'])


            return clientes_data

        
        except:
            raise Exception("Algo de errado ocorreu revise o arquivo json e tente novamente")


