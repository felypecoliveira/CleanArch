from src.infra.tests.contato_repository import ContatosRepositorySpy
from addcontato_to_cliente import AddContatoCliente


def test_addcontato_to_cliente():
    nome_contato = "Julio Isac Garcia"
    telefone_contato = "62985582079"
    email = "julioisac@hotmail.com"
    fk_id_cliente = 45

    repository = ContatosRepositorySpy()
    registro = AddContatoCliente(repository)

    response = registro.add_contato_to_cliente(fk_id_cliente,
                                               nome_contato,
                                               telefone_contato,
                                               email)

    assert repository.insert["nome_contato"] == nome_contato
    assert response["attributes"]["nome_contato"] == nome_contato
    assert response["attributes"]["telefone_contato"] == telefone_contato
    assert response["attributes"]["email"] == email
    assert response["attributes"]["id_cliente"] == fk_id_cliente
    assert response["type"] == "contato_do_cliente"

