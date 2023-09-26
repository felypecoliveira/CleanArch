from src.usecase.contatos.select_contato import SelectContato
from src.domain.repository.contatos_repository import ContatosRepository



def select_contato():
    contato_repository = ContatosRepository()
    usecase_select_contato = SelectContato(contato_repository)
    return usecase_select_contato



select_contato_composer().select_contato(22)

