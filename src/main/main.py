from src.domain.core.contatos_core import Contatos
from src.domain.core.clientes_core import Clientes
from src.main.service import *


def main():
    config_ioc()
    linked_instance()
    service = Service()
    service.select_contato()
    service.get_contatos(Contatos)
    service.get_clientes(Clientes)
