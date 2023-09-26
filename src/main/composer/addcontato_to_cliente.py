from src.domain.repository.contatos_repository import ContatosRepository
from src.usecase.contatos.addcontato_to_cliente import AddContatoCliente



def contatct_costumer():
    contatos_repository = ContatosRepository()
    contato__cliente = AddContatoCliente(contatos_repository)


    return contato__cliente

