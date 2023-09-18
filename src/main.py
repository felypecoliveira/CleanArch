from src.adapter.adpt_contatos.pg_contatos import PostgresAdptContatos,register_ioc_contatos
from src.adapter.adpt_clientes.pg_clientes import PostgresAdptClientes,register_ioc_clientes
from src.domain.core.clientes_core import Clientes




if __name__ == '__main__':
    register_ioc_clientes()
    adapt_clientes = PostgresAdptClientes()
    adapt_contatos = PostgresAdptContatos()

    # pipeline para uso dos metodos disponiveis nas instancias
    adapt_clientes.get_clientes(Clientes)








