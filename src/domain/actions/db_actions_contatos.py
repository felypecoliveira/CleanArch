from src.interfaces.contatos_interface import DbInterfaceContatos
import inject


class DbActionsContatos:
    @inject.autoparams()
    def __init__(self,db_contatos:DbInterfaceContatos):
        self.db_contatos = db_contatos