from src.adapter.adpt_contatos.pg_contatos import PostgresAdptContatos
from src.adapter.adpt_clientes.pg_clientes import PostgresAdptClientes, register_ioc_clientes
from src.domain.core.clientes_core import Clientes

# from src.domain.core.contatos_core import Contatos


if __name__ == '__main__':
    register_ioc_clientes()
    adapt_clientes = PostgresAdptClientes()
    adapt_contatos = PostgresAdptContatos()

    # pipeline para uso dos metodos disponiveis nas instancias

    adapt_clientes.get_clientes(Clientes)

    # adapt_clientes.update_cliente(13,
    #                               Clientes,
    #                               'nome',
    #                               'Nelson Hernandez
    #                               Silva Pereira')
    #
