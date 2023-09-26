from src.domain.repository.clientes_repository import ClientesRepository
from src.usecase.clientes.get_cliente_contatos import GetClientesContatos



def all_clientes_contatos():
    clientes_repository = ClientesRepository()
    get_the_match_child_tb = GetClientesContatos(clientes_repository)


    return get_the_match_child_tb





