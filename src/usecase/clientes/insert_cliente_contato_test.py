from src.infra.tests.cliente_repository import ClientesRespositorySpy
from insert_cliente_contato import InsertClienteContato
from faker import Faker

fake = Faker("pt_BR")


def test_insert_cliente_contato():
    nome = "ANDRE FELYPE"
    telefone = "62985785227"
    cpf = "05110918180"
    endereco = fake.address()
    data_nascimento = "1998-08-31"

    nome_contato = "REBECA CAMARGO"
    telefone_contato = "62995474063"
    email = fake.email()

    repository = ClientesRespositorySpy()
    registro = InsertClienteContato(repository)

    response = registro.insert_cliente_contato(nome,
                                               telefone,
                                               cpf,
                                               endereco,
                                               data_nascimento,
                                               nome_contato,
                                               telefone_contato,
                                               email)

    assert repository.insert["nome"] == nome
    assert response["attributes"]["nome"] == nome
    assert response["attributes"]["telefone"] == telefone
    assert response["attributes"]["cpf"] == cpf
    assert response["type"] == "clientes_contatos"


def test_error_nome_insert_cliente():
    nome = "Andre-"
    telefone = "62985785227"
    cpf = "05110918180"
    endereco = "Senador Canedo Bonfimnopolis,1090"
    data_nascimento = "1998-08-25"

    nome_contato = "REBECA CAMARGO"
    telefone_contato = "62995474063"
    email = fake.email()

    repository = ClientesRespositorySpy()
    registro = InsertClienteContato(repository)

    try:
        response = registro.insert_cliente_contato(nome,
                                                   telefone,
                                                   cpf,
                                                   endereco,
                                                   data_nascimento,
                                                   nome_contato,
                                                   telefone_contato,
                                                   email)
        print("\n")
        print(response["message"])

    except:
        print(response)


def test_error_telefone_cliente():
    nome = "Andre Felype Camargo Oliveira"
    telefone = "629857852278@#"
    cpf = "05110918180"
    endereco = "Senador Canedo Bonfimnopolis,1090"
    data_nascimento = "1998-08-25"

    nome_contato = "REBECA CAMARGO"
    telefone_contato = "62995474063"
    email = fake.email()

    repository = ClientesRespositorySpy()
    registro = InsertClienteContato(repository)

    try:
        response = registro.insert_cliente_contato(nome,
                                                   telefone,
                                                   cpf,
                                                   endereco,
                                                   data_nascimento,
                                                   nome_contato,
                                                   telefone_contato,
                                                   email)
        print("\n")
        print(response["message"])

    except:
        print(response)


def test_error_cpf():
    nome = "Andre Felype Camargo Oliveira"
    telefone = "62985785227"
    cpf = "051.109.181.80"
    endereco = "Senador Canedo Bonfimnopolis,1090"
    data_nascimento = "1998-08-15"

    nome_contato = "REBECA CAMARGO"
    telefone_contato = "62995474063"
    email = fake.email()

    repository = ClientesRespositorySpy()
    registro = InsertClienteContato(repository)

    try:
        response = registro.insert_cliente_contato(nome,
                                                   telefone,
                                                   cpf,
                                                   endereco,
                                                   data_nascimento,
                                                   nome_contato,
                                                   telefone_contato,
                                                   email)
        print("\n")
        print(response["message"])

    except:
        print(response)


def test_error_data_nascimento():
    nome = "Andre Felype Camargo Oliveira"
    telefone = "62985785227"
    cpf = "05110918180"
    endereco = "Senador Canedo Bonfimnopolis,1090"
    data_nascimento = "1998-55-5514"

    nome_contato = "REBECA CAMARGO"
    telefone_contato = "62995474063"
    email = fake.email()

    repository = ClientesRespositorySpy()
    registro = InsertClienteContato(repository)

    try:
        response = registro.insert_cliente_contato(nome,
                                                   telefone,
                                                   cpf,
                                                   endereco,
                                                   data_nascimento,
                                                   nome_contato,
                                                   telefone_contato,
                                                   email)
        print("\n")
        print(response["message"])

    except:
        print(response)
