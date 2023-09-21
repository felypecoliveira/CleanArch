from src.services.service import *


def main():
    config_ioc()
    linked_instance()
    service = Service()
    service.get_contatos(Contatos)


